"""
Beyond the Canvas — Live Demo Server
Run: python server.py
Then open: http://localhost:5000
"""

import os, io, base64, json
import numpy as np
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from PIL import Image

# ── Load model ────────────────────────────────────────────────────────────────
import tensorflow as tf
from tensorflow.keras.models import load_model

MODEL_PATH = "best_final_model.keras"   # ← change if your file is named differently
CLASS_NAMES = ["angry", "fear", "happy", "sad"]   # alphabetical = Keras default order
PALETTE = {"happy": "#4CAF50", "angry": "#F44336",
           "sad": "#2196F3",   "fear":  "#FF9800"}
IMG_SIZE = (224, 224)

print("Loading model…")
model = load_model(MODEL_PATH)
print("Model ready ✓")

app = Flask(__name__, static_folder=".")
CORS(app)

# ── Routes ────────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files["image"]
    img  = Image.open(io.BytesIO(file.read())).convert("RGB").resize(IMG_SIZE)
    arr  = np.array(img, dtype=np.float32) / 255.0
    arr  = np.expand_dims(arr, axis=0)

    preds      = model.predict(arr, verbose=0)[0]
    pred_idx   = int(np.argmax(preds))
    pred_class = CLASS_NAMES[pred_idx]
    confidence = float(preds[pred_idx])

    probs = {CLASS_NAMES[i]: float(preds[i]) for i in range(len(CLASS_NAMES))}

    return jsonify({
        "prediction": pred_class,
        "confidence": confidence,
        "probabilities": probs,
        "color": PALETTE.get(pred_class, "#888")
    })

if __name__ == "__main__":
    app.run(debug=False, port=5000)
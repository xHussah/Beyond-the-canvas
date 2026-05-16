# Beyond the Canvas: Using Machine Learning to Detect Psychological Signals in Children’s Drawings 

## Abstract
This project explores whether machine learning can detect emotional states in children's drawings as a non-intrusive psychological screening tool. Given a drawing image, the system classifies it into one of four emotions: Happy, Angry, Sad, or Fear. 

Five models were compared, SVM with HOG features, MobileNetV2, ResNet50, VGG16, and a Soft-Voting Ensemble. With VGG16 achieving the best performance (60.56% accuracy, macro F1 = 0.61). The solution is deployed as a live web interface where users upload a drawing and receive an instant emotion prediction with confidence scores.

## Dataset
The Children's Drawings Emotion Dataset is a collection of RGB images of children's drawings categorized into four emotional classes: Happy, Angry, Sad, and Fear.

Source: Kaggle - https://www.kaggle.com/datasets/vishmiperera/children-drawings?resource=download 

## Technologies Used

**Language & Framework:**
- Python
- TensorFlow / Keras
- Flask ( web backend server)
- HTML / CSS / JavaScript (web frontend)

**Models Tested**
 
| Model | Test Accuracy | Macro F1 |
|---|---|---|
| SVM with HOG Features (Baseline) | 48.59% | 0.4871 |
| MobileNetV2 | 50.00% | 0.4906 |
| ResNet50 | 32.39% | 0.2609 |
| **VGG16  (Best)** | **60.56%** | **0.6068** |
| Soft-Voting Ensemble | 60.56% | 0.5992 |

## Live Demo 
The live demo is deployed using the best model
<img width="800" alt="Screenshot 2026-05-16 061312" src="https://github.com/user-attachments/assets/a25ec6a0-8784-48ed-9973-96843be1cc9e" />
<img width="800" alt="Screenshot 2026-05-16 061334" src="https://github.com/user-attachments/assets/c14d9c5b-fe97-47b1-a8f7-96c1b14d6538" />
<img width="800" alt="Screenshot 2026-05-16 061357" src="https://github.com/user-attachments/assets/2f71e240-0833-4bb5-bb7c-e52ee5e0c981" />

## Developers
- Deema Alfarhoud
- Renad Alowais
- Hussah Alotaibi 
- Zuhd Ibrahim

This project was finished in May 2026.

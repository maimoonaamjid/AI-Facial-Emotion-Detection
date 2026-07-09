# 😊 AI-Based Facial Emotion Detection System

<p align="center">
  <img src="github-banner.png" width="100%">
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange?style=for-the-badge&logo=tensorflow)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv)
![CNN](https://img.shields.io/badge/CNN-Neural%20Network-red?style=for-the-badge)
![AI](https://img.shields.io/badge/Artificial-Intelligence-purple?style=for-the-badge)

</p>

---

# 📖 Overview

The **AI-Based Facial Emotion Detection System** is a Deep Learning project developed to recognize human facial expressions in real time using Computer Vision and Convolutional Neural Networks (CNN).

The application captures live video through a webcam, detects a person's face using OpenCV, preprocesses the facial image, and predicts the user's emotional state using a trained CNN model.

The project demonstrates the practical implementation of Artificial Intelligence, Machine Learning, Deep Learning, and Computer Vision in Human-Computer Interaction.

---

# ✨ Features

✔ Real-Time Emotion Detection

✔ Face Detection using OpenCV

✔ Deep Learning based CNN Model

✔ FER2013 Emotion Dataset

✔ Live Webcam Prediction

✔ Fast Image Processing

✔ Seven Emotion Categories

✔ User-Friendly Interface

---

# 🎯 Emotion Classes

| Emotion | Description |
|----------|-------------|
| 😠 Angry | Detects anger expressions |
| 🤢 Disgust | Detects disgust expressions |
| 😨 Fear | Detects fear expressions |
| 😀 Happy | Detects smiling and happiness |
| 😐 Neutral | Detects neutral face |
| 😢 Sad | Detects sadness |
| 😲 Surprise | Detects surprised expression |

---

# 🧠 Technologies Used

- Python
- TensorFlow
- Keras
- OpenCV
- NumPy
- Scikit-Learn
- Matplotlib
- Pillow

---

# 🏗 Project Architecture

```
          FER2013 Dataset
                  │
                  ▼
      Image Preprocessing
                  │
                  ▼
      Resize (48 × 48 Pixels)
                  │
                  ▼
        Normalize Images
                  │
                  ▼
      CNN Model Training
                  │
                  ▼
      Save Trained Model
                  │
                  ▼
      Webcam Face Detection
                  │
                  ▼
      Emotion Prediction
                  │
                  ▼
      Display Result
```

---

# 🔄 Project Workflow

```
Dataset Collection
        │
        ▼
Data Preprocessing
        │
        ▼
Image Normalization
        │
        ▼
CNN Training
        │
        ▼
Model Evaluation
        │
        ▼
Save Model (.keras)
        │
        ▼
Real-Time Webcam Prediction
```

---

# 🖥 CNN Model Architecture

```
Input Layer
48 × 48 Grayscale Image

        │

Conv2D

        │

ReLU

        │

MaxPooling

        │

Conv2D

        │

ReLU

        │

MaxPooling

        │

Flatten

        │

Dense Layer

        │

Dropout

        │

Output Layer
Softmax (7 Classes)
```

---

# 📂 Project Structure

```
AI-Facial-Emotion-Detection
│
├── assets/
│   ├── banner.png
│   ├── workflow.png
│   ├── architecture.png
│   └── screenshots/
│
├── dataset/
│   └── train/
│
├── trained_model/
│   └── emotion_model.keras
│
├── notebooks/
│
├── preprocess_data.py
├── train_model.py
├── predict_emotion.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Dataset

This project uses the **FER2013 (Facial Expression Recognition 2013)** dataset.

Dataset Characteristics

- 7 Emotion Classes
- Grayscale Images
- Resolution: **48 × 48**
- Facial Expression Images
- Deep Learning Ready

---

# ⚙ Installation

Clone Repository

```bash
git clone https://github.com/YourUsername/AI-Facial-Emotion-Detection.git
```

Go to Project

```bash
cd AI-Facial-Emotion-Detection
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Running the Project

## Step 1

Preprocess Dataset

```bash
python preprocess_data.py
```

---

## Step 2

Train CNN Model

```bash
python train_model.py
```

---

## Step 3

Start Real-Time Emotion Detection

```bash
python predict_emotion.py
```

---

# 📈 Model Output

The system predicts one of the following emotions in real time:

```
Happy
Neutral
Sad
Angry
Fear
Disgust
Surprise
```

Each prediction includes the confidence score.

Example:

```
😊 Happy (96.24%)

😢 Sad (92.15%)

😠 Angry (88.73%)
```

---

# 📸 Screenshots

### Home

<img src="assets/screenshot1.png" width="800">

---

### Live Detection

<img src="assets/screenshot2.png" width="800">

---

# 🎥 Live Demo

A live webcam demonstration is included with the project presentation.

The application:

- Detects Faces
- Predicts Emotion
- Displays Confidence Score
- Updates in Real Time

---

# 🎯 Applications

- Human Computer Interaction
- Smart Attendance Systems
- Mental Health Monitoring
- Driver Monitoring Systems
- Online Education
- Healthcare
- Security Systems
- Customer Experience Analysis

---

# 🚀 Future Improvements

- Mobile Application
- Higher Accuracy CNN
- FER+ Dataset Support
- Voice Emotion Recognition
- Multiple Face Detection
- Cloud Deployment
- Mobile Camera Support
- GUI Application
- Emotion Analytics Dashboard

---

# 👩‍💻 Authors

### Maimoona Amjid

**FA24-BSE-065**

Software Engineering

---

### Syeda Rabail Fatima

**FA24-BSE-086**

Software Engineering

---

# 🎓 Academic Information

**Course**

Artificial Intelligence

**Course Instructor**

Mam. Aisha

---

# 📄 License

This project is developed for educational and academic purposes.

Licensed under the MIT License.

---

# ⭐ Support

If you like this project,

⭐ Star this repository

🍴 Fork this repository

💡 Feel free to contribute and improve the project.

---

<p align="center">

**Thank You ❤️**

Made with Python, TensorFlow and OpenCV

</p>

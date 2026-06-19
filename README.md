# 🧠 Talk2Mind – AI-Based Mental Well-Being Assessment System

## 📌 Project Overview

Talk2Mind is a Multimodal AI-Based Mental Well-Being Assessment and Support System designed to analyze a user's mental wellness using multiple sources of information such as questionnaire responses, facial emotions, and speech emotions.

The system generates a Mental Well-Being Score and provides personalized recommendations to help users improve their emotional and mental health.

---

## 🎯 Objectives

* Assess mental well-being using AI techniques.
* Analyze facial expressions for emotional understanding.
* Analyze speech signals to detect emotions.
* Evaluate questionnaire responses related to mental health.
* Generate a comprehensive Mental Well-Being Score.
* Provide personalized recommendations for improvement.

---

## ✨ Features

### 1. Questionnaire-Based Assessment

* Stress Level Analysis
* Sleep Quality Analysis
* Anxiety Level Analysis
* Happiness Level Analysis
* Burnout Level Analysis

### 2. Facial Emotion Analysis

* Upload face images
* Detect facial emotions
* Emotion-based scoring

### 3. Speech Emotion Analysis

* Upload audio files
* Detect speech emotions
* Emotion-based scoring

### 4. Feature Fusion

Combines:

* Questionnaire Score
* Face Emotion Score
* Speech Emotion Score

to generate a final Mental Well-Being Score.

### 5. Recommendation Engine

Provides personalized suggestions based on the final score.

### 6. Assessment History

Stores previous assessment results using SQLite database.

---

## 🏗️ Project Structure

Talk2Mind/

├── app.py

├── questionnaire.py

├── recommendation.py

├── fusion.py

├── face_emotion.py

├── speech_emotion.py

├── database.py

├── requirements.txt

├── README.md

├── results.db

├── assets/

├── datasets/

└── models/

---

## 🛠️ Technologies Used

* Python
* Streamlit
* SQLite
* NumPy
* Pandas
* Matplotlib
* Scikit-Learn
* Librosa
* OpenCV
* DeepFace

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Rishika14104/TIME2MIND.git
```

Move into the project folder:

```bash
cd TIME2MIND
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
streamlit run app.py
```

---

## 📊 Workflow

1. User enters questionnaire responses.
2. User uploads face image.
3. User uploads speech/audio file.
4. System extracts emotional information.
5. Feature fusion module combines all inputs.
6. Mental Well-Being Score is generated.
7. Personalized recommendations are displayed.
8. Results are stored for future reference.

---

## 📈 Expected Outcome

The system helps users:

* Understand their mental wellness status.
* Identify stress and emotional concerns early.
* Track mental well-being over time.
* Receive personalized wellness recommendations.

---

## 👩‍💻 Developer

Kosireddy Rishika

B.Tech Graduate

Project: Talk2Mind – AI-Based Mental Well-Being Assessment System

---

## 📜 License

This project is developed for academic and educational purposes.

---

## Outputs

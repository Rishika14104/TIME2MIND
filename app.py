import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

from questionnaire import calculate_questionnaire_score
from recommendation import get_recommendation
from fusion import emotion_score, calculate_final_score
from database import create_table, save_result

# Create database table
create_table()

st.set_page_config(
    page_title="Talk2Mind",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Talk2Mind")
st.subheader("AI-Based Mental Wellbeing Assessment System")

st.markdown("---")

# ==========================
# Questionnaire Section
# ==========================

st.header("📋 Questionnaire Assessment")

stress = st.slider("Stress Level", 1, 5, 3)
sleep = st.slider("Sleep Quality", 1, 5, 3)
anxiety = st.slider("Anxiety Level", 1, 5, 3)
happiness = st.slider("Happiness Level", 1, 5, 3)
burnout = st.slider("Burnout Level", 1, 5, 3)

st.markdown("---")

# ==========================
# Face Emotion Section
# ==========================

st.header("😊 Facial Emotion Analysis")

uploaded_image = st.file_uploader(
    "Upload Face Image",
    type=["jpg", "jpeg", "png"]
)

face_emotion = "Neutral"

if uploaded_image is not None:

    st.image(
        uploaded_image,
        caption="Uploaded Image",
        width=300
    )

    if st.button("Detect Face Emotion"):

        # Replace with DeepFace later
        face_emotion = "Happy"

        st.success(
            f"Detected Face Emotion: {face_emotion}"
        )

st.markdown("---")

# ==========================
# Speech Emotion Section
# ==========================

st.header("🎤 Speech Emotion Analysis")

audio_file = st.file_uploader(
    "Upload Audio File",
    type=["wav", "mp3"]
)

speech_emotion = "Neutral"

if audio_file is not None:

    if st.button("Detect Speech Emotion"):

        # Replace with actual prediction later
        speech_emotion = "Happy"

        st.success(
            f"Detected Speech Emotion: {speech_emotion}"
        )

st.markdown("---")

# ==========================
# Final Assessment
# ==========================

if st.button("Generate Assessment"):

    questionnaire_score = calculate_questionnaire_score(
        stress,
        sleep,
        anxiety,
        happiness,
        burnout
    )

    face_score = emotion_score(face_emotion)

    speech_score = emotion_score(speech_emotion)

    final_score = calculate_final_score(
        questionnaire_score,
        face_score,
        speech_score
    )

    save_result(
        questionnaire_score,
        face_score,
        speech_score,
        final_score
    )

    st.success("Assessment Generated Successfully")

    st.markdown("## 📊 Scores")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Questionnaire Score",
            questionnaire_score
        )

        st.metric(
            "Face Score",
            face_score
        )

    with col2:
        st.metric(
            "Speech Score",
            speech_score
        )

        st.metric(
            "Final Wellbeing Score",
            final_score
        )

    st.progress(int(final_score))

    st.markdown("## 💡 Recommendation")

    recommendation = get_recommendation(
        final_score
    )

    st.write(recommendation)

    # Pie Chart

    fig, ax = plt.subplots()

    ax.pie(
        [
            questionnaire_score,
            face_score,
            speech_score
        ],
        labels=[
            "Questionnaire",
            "Face",
            "Speech"
        ],
        autopct="%1.1f%%"
    )

    st.pyplot(fig)

    if final_score >= 80:
        st.balloons()

st.markdown("---")

# ==========================
# Assessment History
# ==========================

st.header("📜 Assessment History")

conn = sqlite3.connect(
    "results.db"
)

df = pd.read_sql(
    "SELECT * FROM assessments",
    conn
)

st.dataframe(df)

conn.close()
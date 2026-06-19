from deepface import DeepFace
import tempfile


def detect_face_emotion(uploaded_file):
    try:
        # Save uploaded image temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
            tmp_file.write(uploaded_file.read())
            file_path = tmp_file.name

        # Analyze emotion
        result = DeepFace.analyze(
            img_path=file_path,
            actions=["emotion"],
            enforce_detection=False
        )

        emotion = result[0]["dominant_emotion"]

        return emotion

    except Exception as e:
        return f"Error: {str(e)}"
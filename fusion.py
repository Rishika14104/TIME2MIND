def emotion_score(emotion):

    scores = {

        "Happy": 90,
        "Neutral": 75,
        "Sad": 40,
        "Angry": 30,
        "Fear": 35,
        "Surprise": 80

    }

    return scores.get(
        emotion,
        50
    )


def calculate_final_score(
    questionnaire_score,
    face_score,
    speech_score
):

    final_score = (
        0.4 * questionnaire_score +
        0.3 * face_score +
        0.3 * speech_score
    )

    return round(
        final_score,
        2
    )
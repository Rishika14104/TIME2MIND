import sqlite3

def create_table():

    conn = sqlite3.connect("results.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS assessments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        questionnaire_score REAL,
        face_score REAL,
        speech_score REAL,
        final_score REAL
    )
    """)

    conn.commit()
    conn.close()


def save_result(
    questionnaire_score,
    face_score,
    speech_score,
    final_score
):

    conn = sqlite3.connect("results.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO assessments(
        questionnaire_score,
        face_score,
        speech_score,
        final_score
    )
    VALUES(?,?,?,?)
    """,
    (
        questionnaire_score,
        face_score,
        speech_score,
        final_score
    ))

    conn.commit()
    conn.close()
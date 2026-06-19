def calculate_questionnaire_score(
    stress,
    sleep,
    anxiety,
    happiness,
    burnout
):

    score = (
        (6 - stress)
        + sleep
        + (6 - anxiety)
        + happiness
        + (6 - burnout)
    )

    percentage = (score / 25) * 100

    return round(percentage, 2)
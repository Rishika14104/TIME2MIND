def get_recommendation(score):

    if score >= 80:
        return """
Excellent Mental Wellbeing

• Continue healthy habits
• Maintain regular sleep
• Exercise regularly
"""

    elif score >= 60:
        return """
Moderate Wellbeing

• Practice meditation
• Reduce stress
• Improve sleep quality
"""

    else:
        return """
Needs Attention

• Manage stress actively
• Seek support from friends/family
• Consider professional guidance
"""
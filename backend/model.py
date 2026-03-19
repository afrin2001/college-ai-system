# Placeholder for ML model if needed later
def predict_student_risk(data):
    if data.get("attendance", 100) < 50:
        return "At Risk"
    return "Safe"

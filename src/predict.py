import joblib
import pandas as pd

def predict():
    model = joblib.load("models/model.pkl")

    new_student = pd.DataFrame({
        "study_hours": [6],
        "attendance": [85],
        "previous_marks": [75],
        "sleep_hours": [7]
    })

    result = model.predict(new_student)
    print("Predicted Score:", result[0])

if __name__ == "__main__":
    predict()
import pandas as pd
import numpy as np

def generate_data(size=200):
    np.random.seed(42)

    data = pd.DataFrame({
        "study_hours": np.random.randint(1, 10, size),
        "attendance": np.random.randint(50, 100, size),
        "previous_marks": np.random.randint(40, 100, size),
        "sleep_hours": np.random.randint(4, 10, size),
    })

    data["final_score"] = (
        data["study_hours"] * 5 +
        data["attendance"] * 0.3 +
        data["previous_marks"] * 0.4 +
        data["sleep_hours"] * 2 +
        np.random.randint(-10, 10, size)
    )

    return data
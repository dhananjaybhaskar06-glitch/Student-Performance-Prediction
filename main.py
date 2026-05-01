import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# ==============================
# 1. CREATE DATA
# ==============================
np.random.seed(42)
data_size = 200

data = pd.DataFrame({
    "study_hours": np.random.randint(1, 10, data_size),
    "attendance": np.random.randint(50, 100, data_size),
    "previous_marks": np.random.randint(40, 100, data_size),
    "sleep_hours": np.random.randint(4, 10, data_size),
})

data["final_score"] = (
    data["study_hours"] * 5 +
    data["attendance"] * 0.3 +
    data["previous_marks"] * 0.4 +
    data["sleep_hours"] * 2 +
    np.random.randint(-10, 10, data_size)
)

print("\nSample Data:\n", data.head())

# ==============================
# 2. SPLIT DATA
# ==============================
X = data.drop("final_score", axis=1)
y = data["final_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==============================
# 3. TRAIN MULTIPLE MODELS
# ==============================
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(),
    "Random Forest": RandomForestRegressor()
}

results = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    results[name] = r2

    print(f"\n{name} Results:")
    print("MAE:", mae)
    print("R2 Score:", r2)

# ==============================
# 4. BEST MODEL SELECTION
# ==============================
best_model_name = max(results, key=results.get)
best_model = models[best_model_name]

print(f"\nBest Model: {best_model_name}")

# ==============================
# 5. SAVE MODEL
# ==============================
joblib.dump(best_model, "models/best_model.pkl")
print("Model saved in models/best_model.pkl")

# ==============================
# 6. PLOT MODEL COMPARISON
# ==============================
plt.bar(results.keys(), results.values())
plt.title("Model Comparison (R2 Score)")
plt.ylabel("R2 Score")
plt.xticks(rotation=20)
plt.savefig("outputs/model_comparison.png")
plt.show()

# ==============================
# 7. FEATURE IMPORTANCE (Only for RF)
# ==============================
if best_model_name == "Random Forest":
    importance = best_model.feature_importances_
    features = X.columns

    plt.bar(features, importance)
    plt.title("Feature Importance")
    plt.savefig("outputs/feature_importance.png")
    plt.show()

# ==============================
# 8. PREDICT NEW STUDENT
# ==============================
new_student = pd.DataFrame({
    "study_hours": [6],
    "attendance": [85],
    "previous_marks": [75],
    "sleep_hours": [7]
})

prediction = best_model.predict(new_student)
print("\nPredicted Score:", prediction[0])
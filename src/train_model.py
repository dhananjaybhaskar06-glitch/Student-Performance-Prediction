import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

from data_processing import generate_data

def train():
    data = generate_data()

    X = data.drop("final_score", axis=1)
    y = data["final_score"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("R2 Score:", r2_score(y_test, y_pred))

    joblib.dump(model, "models/model.pkl")
    print("Model saved!")

if __name__ == "__main__":
    train()
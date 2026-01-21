from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle
from src.data_preprocessing import load_data

def train_model():
    X, y = load_data()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    pickle.dump(model, open("models/linear_regression_model.pkl", "wb"))
    print("✅ Model trained and saved successfully")

    return model





import pickle
import numpy as np

def predict_score(hours, attendance, previous_score):
    model = pickle.load(open("models/linear_regression_model.pkl", "rb"))
    data = np.array([[hours, attendance, previous_score]])
    prediction = model.predict(data)
    return prediction[0]

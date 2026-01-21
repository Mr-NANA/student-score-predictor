import pandas as pd

def load_data():
    data = pd.read_csv("data/student_scores.csv")
    X = data[['hours_studied', 'attendance', 'previous_score']]
    y = data['final_score']
    return X, y


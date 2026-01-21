from src.predict import predict_score

hours = float(input("Enter hours studied: "))
attendance = float(input("Enter attendance %: "))
previous = float(input("Enter previous score: "))

result = predict_score(hours, attendance, previous)

print("Predicted Final Score:", round(result, 2))

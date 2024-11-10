import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

model = joblib.load('spam_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

emails = ["Win a million dollars now!", "Meeting at 3 PM", "Important bank update", "Exclusive offer just for you"]
labels = [1, 0, 0, 1]  # if 1 it's spam, else not spam

X_test = vectorizer.transform(emails) 


y_pred = model.predict(X_test)


accuracy = accuracy_score(labels, y_pred)
precision = precision_score(labels, y_pred)
recall = recall_score(labels, y_pred)
f1 = f1_score(labels, y_pred)


performance_data = {
    "Metric": ["Accuracy", "Precision", "Recall", "F1-Score"],
    "Score": [accuracy, precision, recall, f1]
}

df_performance = pd.DataFrame(performance_data)
print("Performance Metrics:\n", df_performance)


print("\nClassification Report:\n", classification_report(labels, y_pred))

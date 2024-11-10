import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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


plt.figure(figsize=(10, 6))
sns.barplot(x='Metric', y='Score', data=df_performance, palette='viridis')
plt.title('Performance Metrics for Spam Classification')
plt.xlabel('Metric')
plt.ylabel('Score')
plt.ylim(0, 1)  
plt.show()


print("\nClassification Report:\n", classification_report(labels, y_pred))

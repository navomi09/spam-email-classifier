import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

emails = ["Win a million dollars now!", "Meeting at 3 PM", "Important bank update", "Exclusive offer just for you"]
labels = [1, 0, 0, 1]  # 1 for spam, 0 for not spam

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=42)


model = MultinomialNB()
model.fit(X_train, y_train)


joblib.dump(model, 'spam_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')


y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

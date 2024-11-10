from flask import Flask, render_template
import joblib
from fetch_emails import fetch_emails  # Import the fetch_emails function

model = joblib.load('spam_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['GET', 'POST'])
def classify():
    emails = fetch_emails()  
    results = []


    for subject, body in emails:
        email_vectorized = vectorizer.transform([body])  
        prediction = model.predict(email_vectorized)  # Classify email
        result = "Spam" if prediction[0] == 1 else "Not Spam"
        results.append((subject, result))


    return render_template('index.html', emails=results)

if __name__ == '__main__':
    app.run(debug=True)

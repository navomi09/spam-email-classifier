from flask import Flask, render_template
import joblib
from fetch_emails import fetch_emails  # Import the fetch_emails function

# Load pre-trained model and vectorizer
model = joblib.load('spam_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['GET', 'POST'])
def classify():
    emails = fetch_emails()  # Fetch the latest emails using the fetch_emails function
    results = []

    # Classify fetched emails
    for subject, body in emails:
        email_vectorized = vectorizer.transform([body])  # Vectorize email body
        prediction = model.predict(email_vectorized)  # Classify email
        result = "Spam" if prediction[0] == 1 else "Not Spam"
        results.append((subject, result))

    # Render results in the web page
    return render_template('index.html', emails=results)

if __name__ == '__main__':
    app.run(debug=True)

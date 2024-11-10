import joblib

model = joblib.load('spam_model.pkl')       
vectorizer = joblib.load('vectorizer.pkl') 


def classify_email(email_text):

    transformed_text = vectorizer.transform([email_text])  

    prediction = model.predict(transformed_text)[0]  
    return "Spam" if prediction == 1 else "Not Spam"

if __name__ == "__main__":

    email_text = "Win a free vacation now!"  
    result = classify_email(email_text) 
    print(f"Email Classification: {result}")  

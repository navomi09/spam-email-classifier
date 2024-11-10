# spam-email-classifier
This project is focused on building a Spam Email Classifier using the Naive Bayes machine learning model. The model is trained to distinguish between spam and ham. Implemented this in a Flask web application, which allows the user to classify emails fetched directly from a Gmail inbox.
We also enhanced the project with Edge Computing principles, enabling classification to be performed closer to the data source  improving response times and privacy by processing data locally instead of sending it to the cloud.

**Project Flow:**
1.	Email Fetching:
- Emails are fetched from a Gmail inbox using IMAP (Internet Message Access Protocol) and Python's imaplib. 
2.	Email Classification with Naive Bayes:
- The emails are processed using a Naive Bayes classifier. We use the Multinomial Naive Bayes model from the scikit-learn library.
- CountVectorizer is used to convert the email text into numerical vectors (features) that the Naive Bayes model can understand.
- The classifier was trained on a dataset where emails are labeled as either spam (1) or non-spam (0).
3.	Flask Web Application:
- A simple Flask web app was created to display the results of the classification. It fetches the emails, processes them, and shows whether each email is spam or not spam on the webpage.
4.	Edge Computing Concept:
- The email classification process can be considered an Edge Computing application since the model is hosted and executed locally, closer to the data source (on the user’s machine or a local server), rather than relying on a central cloud server.
- This reduces latency because classification happens immediately after email fetching. It also increases privacy by not sending sensitive email data to the cloud.

**Libraries and Technologies Used:**
1.	Flask:
- Flask is a lightweight Python web framework used to create the web application. It allows us to create routes, manage HTTP requests, and render HTML templates.
- Flask also helps integrate the model with the web interface, so users can interact with the system.
2.	Scikit-learn:
- Scikit-learn provides the Naive Bayes algorithm used to classify emails. The Multinomial Naive Bayes model was chosen because it works well with text data, especially in spam classification tasks.
- CountVectorizer is used to convert the raw email text into numerical features, which can then be fed into the Naive Bayes model for prediction.
3.	IMAP and Email Libraries:
- imaplib and email libraries are used to connect to Gmail via IMAP and fetch emails. These libraries allow us to access the inbox, retrieve email metadata (such as subject), and extract the email body content.
- The decode_header function from the email.header module is used to decode email subject lines, which may be encoded in various character sets.
4.	Dotenv:
- dotenv is used to store email credentials securely in a .env file, which helps avoid hardcoding sensitive information in the source code. This improves security by ensuring that credentials are not exposed publicly.
5.	Joblib:
- Joblib is used to serialize (save) the trained model and vectorizer to disk, so they can be reused without needing to retrain the model each time the application runs.

**How It Works:**
1.	Fetching Emails:
- The fetch_emails() function connects to Gmail using IMAP, fetches the latest unread emails, and extracts their subject and body.
- These emails are then returned as a list of tuples (subject, body) to be classified.
2.	Classifying Emails:
- The emails are passed through the Naive Bayes model for classification. The body of each email is transformed into a vector using CountVectorizer, and the model predicts whether the email is spam or not based on its content.
- The results (Spam or Not Spam) are stored and displayed in the web interface.
3.	Displaying Results:
-	The Flask web app displays the classification results on a simple HTML page, showing the subject of the email and whether it’s classified as Spam or Not Spam.

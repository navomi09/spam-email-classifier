import os
from dotenv import load_dotenv
import imaplib
import email
from email.header import decode_header

# Load environment variables
load_dotenv()

def fetch_emails():
    email_user = os.getenv('EMAIL_USER')
    email_pass = os.getenv('EMAIL_PASS')
    
    # Connect to email server
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(email_user, email_pass)
    mail.select('inbox')

    # Fetch all emails (you can also filter for unseen emails)
    _, messages = mail.search(None, 'UNSEEN')  # Fetch only unread emails
    email_ids = messages[0].split()

    emails = []
    for e_id in email_ids[-5:]:  # Fetch last 5 emails (change if needed)
        _, data = mail.fetch(e_id, '(RFC822)')
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)

        # Decode the email subject
        subject, encoding = decode_header(msg['Subject'])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else 'utf-8')

        # Get email body (plaintext)
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode("utf-8")
        else:
            body = msg.get_payload(decode=True).decode("utf-8")

        emails.append((subject, body))  # Store subject and body

    mail.logout()
    return emails

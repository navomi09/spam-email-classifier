import os
from dotenv import load_dotenv
import imaplib
import email
from email.header import decode_header

load_dotenv()

def fetch_emails():
    email_user = os.getenv('EMAIL_USER')
    email_pass = os.getenv('EMAIL_PASS')
    

    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(email_user, email_pass)
    mail.select('inbox')

    _, messages = mail.search(None, 'UNSEEN')  
    email_ids = messages[0].split()

    emails = []
    for e_id in email_ids[-5:]:  
        _, data = mail.fetch(e_id, '(RFC822)')
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)

        # Decode the email subject
        subject, encoding = decode_header(msg['Subject'])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else 'utf-8')

      
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode("utf-8")
        else:
            body = msg.get_payload(decode=True).decode("utf-8")

        emails.append((subject, body))  
    mail.logout()
    return emails

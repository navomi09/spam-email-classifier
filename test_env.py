from dotenv import load_dotenv
import os

load_dotenv() 
print("Email User:", os.getenv('EMAIL_USER'))
print("Email Pass:", os.getenv('EMAIL_PASS'))

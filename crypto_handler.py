from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("SECRET_KEY").encode()
fernet = Fernet(key)

def encrypt_card(card_number):
    return fernet.encrypt(card_number.encode()).decode()

def decrypt_card(encrypted_card):
    return fernet.decrypt(encrypted_card.encode()).decode()


from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(f"Your secret key: {key}")


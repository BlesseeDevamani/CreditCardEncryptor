from crypto_handler import encrypt_card, decrypt_card
from access_control import authenticate_user

def main():
    print("=== Credit Card Encryptor ===")
    action = input("Do you want to (E)ncrypt or (D)ecrypt? ").lower()
    password = input("Enter admin password: ")

    if not authenticate_user(password):
        print("Access Denied.")
        return

    if action == 'e':
        card_number = input("Enter credit card number: ")
        encrypted = encrypt_card(card_number)
        print(f"Encrypted: {encrypted}")
    elif action == 'd':
        encrypted = input("Enter encrypted data: ")
        try:
            decrypted = decrypt_card(encrypted)
            print(f"Decrypted: {decrypted}")
        except Exception as e:
            print("Decryption failed:", str(e))

if __name__ == "_main_":
    main()


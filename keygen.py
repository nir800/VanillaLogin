from cryptography.fernet import Fernet

def generate_key():
    """
    Generates a random key for password encryption
    """
    key = Fernet.generate_key()
    with open("pass.key", "wb") as key_file:
        key_file.write(key)

generate_key()

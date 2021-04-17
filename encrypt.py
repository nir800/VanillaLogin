from cryptography.fernet import Fernet
def load_key():
    """
    Load password  key
    """
    return open("pass.key", "rb").read()
def encrypt_message(message):
    """
    Encrypts  password
    """
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)

    print(encrypted_message)



mypass = input("What is your password? ")

encrypt_message(mypass)

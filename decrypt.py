from cryptography.fernet import Fernet


def load_key():
    """
    Load password key
    """
    return open("pass.key", "rb").read()

def decrypt_message(encrypted_message):
    """
    Decrypts password
    """

    encrypted_message=bytes(encrypted_message, 'ascii')
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()
    

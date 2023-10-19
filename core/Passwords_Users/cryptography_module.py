from cryptography.fernet import Fernet


def encrypt_password(password: str, key: str) -> str:
    """Encripta la contraseña con la llave dada por el usuario al registrarse en la app"""
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode("utf-8"))
    return encrypted_password.decode("utf-8")


def decrypt_password(encrypted_password: str, key: str) -> str:
    """Desencripta la contraseña con la llave"""
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password.encode("utf-8"))
    return decrypted_password.decode("utf-8")

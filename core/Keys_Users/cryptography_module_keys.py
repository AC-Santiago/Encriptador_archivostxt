from cryptography.fernet import Fernet


def encrypt_keys(personal_key: str, key: str) -> str:
    """Encripta la contraseña con la llave dada por el usuario al registrarse en la app"""
    f = Fernet(key)
    encrypted_keys = f.encrypt(personal_key.encode("utf-8"))
    return encrypted_keys.decode("utf-8")


def decrypt_keys(encrypted_keys: str, key: str) -> str:
    """Desencripta la contraseña con la llave"""
    f = Fernet(key)
    decrypted_keys = f.decrypt(encrypted_keys.encode("utf-8"))
    return decrypted_keys.decode("utf-8")

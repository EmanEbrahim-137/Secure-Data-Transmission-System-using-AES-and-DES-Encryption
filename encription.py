# encrypt.py
import hashlib
import base64
from Crypto.Cipher import AES

DEFAULT_PASSWORD = "strong-password-123"

def _derive_key(password: str) -> bytes:
    return hashlib.sha256(password.encode('utf-8')).digest() 

def encrypt_text(text: str, password: str = DEFAULT_PASSWORD) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    if not isinstance(password, str):
        raise TypeError("password must be a str")

    key = _derive_key(password)            
    plaintext = text.encode('utf-8')       

    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce                    
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    package = nonce + tag + ciphertext

    return base64.b64encode(package).decode('utf-8')


if __name__ == "__main__":
    sample_text = "FCAI Damietta University"
    encrypted = encrypt_text(sample_text)
    print("Base64 ciphertext:")
    print(encrypted)

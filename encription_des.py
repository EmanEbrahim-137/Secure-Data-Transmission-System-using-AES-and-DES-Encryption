# encrypt_des.py
import hashlib
import base64
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

DEFAULT_PASSWORD = "strong-password-123"

def _derive_key(password: str) -> bytes:

    full_hash = hashlib.sha256(password.encode('utf-8')).digest()
    return full_hash[:8]  # DES uses 8-byte keys

def encrypt_text(text: str, password: str = DEFAULT_PASSWORD) -> str:

    if not isinstance(text, str):
        raise TypeError("text must be a str")
    if not isinstance(password, str):
        raise TypeError("password must be a str")

    key = _derive_key(password)            
    plaintext = text.encode('utf-8')       

    cipher = DES.new(key, DES.MODE_CBC)
    iv = cipher.iv                    
    ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))

    package = iv + ciphertext

    return base64.b64encode(package).decode('utf-8')


if __name__ == "__main__":
    sample_text = "FCAI Damietta University"
    encrypted = encrypt_text(sample_text)
    print("Base64 ciphertext:")
    print(encrypted)

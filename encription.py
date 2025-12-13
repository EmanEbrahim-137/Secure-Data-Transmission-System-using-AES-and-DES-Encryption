# encrypt.py
import hashlib
import base64
from Crypto.Cipher import AES

DEFAULT_PASSWORD = "strong-password-123"

def _derive_key(password: str) -> bytes:
    """
    Derive a 32-byte AES key from a password string using SHA-256.
    This makes it easy to pass any password/text as the key.
    """
    return hashlib.sha256(password.encode('utf-8')).digest()  # 32 bytes

def encrypt_text(text: str, password: str = DEFAULT_PASSWORD) -> str:
    """
    Encrypt `text` (str) with AES-EAX using a key derived from `password`.
    Returns a Base64-encoded string that contains: nonce || tag || ciphertext.

    Usage:
        b64 = encrypt_text("hello world", "my secret password")
    """
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    if not isinstance(password, str):
        raise TypeError("password must be a str")

    key = _derive_key(password)             # 32-byte key
    plaintext = text.encode('utf-8')        # handle Unicode

    # Create AES-EAX cipher (authenticated mode)
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce                    # typically 16 bytes
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    # pack: nonce || tag || ciphertext
    package = nonce + tag + ciphertext

    # return Base64 string
    return base64.b64encode(package).decode('utf-8')


if __name__ == "__main__":
    # Quick demonstration when running this file directly
    sample_text = "FCAI Damietta University"
    # Uses default password
    encrypted = encrypt_text(sample_text)
    print("Base64 ciphertext:")
    print(encrypted)

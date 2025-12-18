import hashlib
import base64
from Crypto.Cipher import AES

DEFAULT_PASSWORD = "strong-password-123"

def _derive_key(password: str) -> bytes:
    return hashlib.sha256(password.encode('utf-8')).digest()  

def decrypt_text(ciphertext_b64: str, password: str = DEFAULT_PASSWORD) -> str:
    key = _derive_key(password)

    package = base64.b64decode(ciphertext_b64)
    nonce = package[:16]
    tag = package[16:32]
    ciphertext = package[32:]

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode('utf-8')


if __name__ == "__main__":
    encrypted_text = input("Enter the Base64 encrypted text:\n")
    try:
        decrypted = decrypt_text(encrypted_text)
        print("\nDecrypted text:")
        print(decrypted)
    except ValueError:
        print("Decryption failed: corrupted ciphertext or wrong key")
import hashlib
import base64
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

DEFAULT_PASSWORD = "strong-password-123"

def _derive_key(password: str) -> bytes:
    full_hash = hashlib.sha256(password.encode('utf-8')).digest()
    return full_hash[:8]  

def decrypt_text(ciphertext_b64: str, password: str = DEFAULT_PASSWORD) -> str:
    key = _derive_key(password)

    package = base64.b64decode(ciphertext_b64)
    iv = package[:8]  
    ciphertext = package[8:]

    cipher = DES.new(key, DES.MODE_CBC, iv=iv)
    plaintext = unpad(cipher.decrypt(ciphertext), DES.block_size)
    return plaintext.decode('utf-8')


if __name__ == "__main__":
    encrypted_text = input("Enter the Base64 encrypted text:\n")
    try:
        decrypted = decrypt_text(encrypted_text)
        print("\nDecrypted text:")
        print(decrypted)
    except ValueError:
        print("Decryption failed: corrupted ciphertext or wrong key")

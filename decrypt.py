import hashlib
import base64
from Crypto.Cipher import AES

DEFAULT_PASSWORD = "strong-password-123"

def _derive_key(password: str) -> bytes:
    """
    Derive the same 32-byte AES key from the password using SHA-256.
    """
    return hashlib.sha256(password.encode('utf-8')).digest()  # 32 bytes

def decrypt_text(ciphertext_b64: str, password: str = DEFAULT_PASSWORD) -> str:
    """
    Decrypt a Base64-encoded string produced by encrypt_text().
    Uses the fixed password from the encryption code.
    """
    key = _derive_key(password)

    package = base64.b64decode(ciphertext_b64)
    nonce = package[:16]
    tag = package[16:32]
    ciphertext = package[32:]

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode('utf-8')


# 🔹 طلب النص المشفر من المستخدم
if __name__ == "__main__":
    encrypted_text = input("Enter the Base64 encrypted text:\n")
    try:
        # Uses default password
        decrypted = decrypt_text(encrypted_text)
        print("\nDecrypted text:")
        print(decrypted)
    except ValueError:
        print("Decryption failed: corrupted ciphertext or wrong key")
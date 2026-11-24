# 091 · Security Basics: hashing, secrets and hmac — Example 2: Secure password hashing and verification
# Run: python example_2.py

import hashlib, secrets, hmac

def hash_password(password: str) -> str:
    salt = secrets.token_bytes(16)
    key = hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1)
    return salt.hex() + ":" + key.hex()

def verify_password(password: str, stored: str) -> bool:
    salt_hex, key_hex = stored.split(":")
    key = hashlib.scrypt(password.encode(), salt=bytes.fromhex(salt_hex), n=2**14, r=8, p=1)
    return hmac.compare_digest(key.hex(), key_hex)

stored = hash_password("MyS3cret!")
print("stored:", stored[:50], "...")
print("correct password:", verify_password("MyS3cret!", stored))
print("wrong password  :", verify_password("guess123", stored))
print("same password twice gives different hashes:", hash_password("a") != hash_password("a"))

# Day 104 · Security Basics: hashing, secrets and hmac — secrets tokens and HMAC signatures
# Run: python example_3.py

import secrets, hmac, hashlib, string

print("OTP:", "".join(secrets.choice(string.digits) for _ in range(6)))
print("API key:", secrets.token_urlsafe(24))
alphabet = string.ascii_letters + string.digits + "!@#$%"
print("password:", "".join(secrets.choice(alphabet) for _ in range(14)))

SECRET = b"server-side-secret"
def sign(message: bytes) -> str:
    return hmac.new(SECRET, message, hashlib.sha256).hexdigest()
def verify(message: bytes, signature: str) -> bool:
    return hmac.compare_digest(sign(message), signature)

payload = b'{"order": 42, "amount": 999}'
sig = sign(payload)
print("valid:", verify(payload, sig))
print("tampered:", verify(b'{"order": 42, "amount": 1}', sig))

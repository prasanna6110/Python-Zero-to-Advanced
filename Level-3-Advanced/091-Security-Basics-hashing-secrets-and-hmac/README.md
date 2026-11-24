# 091 · Security Basics: hashing, secrets and hmac

## hashlib: one-way fingerprints
`sha256`, `sha512`, `blake2b`, `md5` (⚠️ md5 and sha1 are broken, so only use them for checksums).
- Uses: file integrity checks, deduplication, cache keys.
- **Passwords**: never store them as plain text or a plain SHA. Use a **slow, salted** function: `hashlib.scrypt` or `pbkdf2_hmac` (or `bcrypt` or `argon2` from PyPI).

## secrets: cryptographically secure randomness
`token_hex`, `token_urlsafe`, `choice`, `randbelow`. Use it for OTPs, reset tokens and API keys. **Never** use `random` for these.

## hmac: message authentication
Proves a message came from someone who knows the key and hasn't been changed. Webhooks and JWTs use it.
Always compare with `hmac.compare_digest`, which runs in constant time and so resists timing attacks.

## More practices
Validate input, never use `eval` on untrusted data, never unpickle untrusted data, use parameterised SQL, and keep secrets in environment variables, not in code.

## Examples

### Example 1: Hashing and file integrity  ([`example_1.py`](example_1.py))

```python
import hashlib

text = "Python Zero to Ultra Advanced"
for algo in ["md5", "sha1", "sha256", "blake2b"]:
    h = hashlib.new(algo, text.encode()).hexdigest()
    print(f"{algo:<8} {h[:40]}...")
print("1 char change:", hashlib.sha256(b"hello").hexdigest()[:16], hashlib.sha256(b"hellp").hexdigest()[:16])

def file_checksum(path, chunk=8192):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while block := f.read(chunk):
            h.update(block)
    return h.hexdigest()

with open("demo.bin", "wb") as f:
    f.write(b"x" * 100_000)
print("file sha256:", file_checksum("demo.bin")[:32])
import os; os.remove("demo.bin")
```

### Example 2: Secure password hashing and verification  ([`example_2.py`](example_2.py))

```python
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
```

### Example 3: secrets tokens and HMAC signatures  ([`example_3.py`](example_3.py))

```python
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
```

## Practice

1. Build a user signup and login system that stores scrypt hashes in SQLite.
2. Write a duplicate-file finder that uses SHA-256.
3. Generate signed "download links" that expire (sign the URL together with a timestamp).

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

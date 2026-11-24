# Day 170 · Project: Password Manager (Encrypted Vault)

_Projects_

**Concepts:** key derivation from a master password (`hashlib.scrypt`), encryption with an HMAC-SHA256 keystream (educational), authenticating data with HMAC, JSON vault files, `getpass`, password generation.

> ⚠️ **This is for learning.** For a real password manager, use `cryptography.fernet` (AES) or a trusted app. The structure here (KDF → encrypt → authenticate) is the same one real tools use.

## Code

### Encrypted Password Vault  ([`main.py`](main.py))

```python
import base64
import getpass
import hashlib
import hmac
import json
import secrets
import string
import sys
from pathlib import Path

DEMO = not sys.stdin.isatty()

def derive_keys(master, salt):
    key = hashlib.scrypt(master.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=64)
    return key[:32], key[32:]                    # an encryption key and a MAC key

def keystream(key, nonce, length):
    out, counter = b"", 0
    while len(out) < length:
        out += hmac.new(key, nonce + counter.to_bytes(8, "big"), hashlib.sha256).digest()
        counter += 1
    return out[:length]

def encrypt(data: bytes, enc_key, mac_key):
    nonce = secrets.token_bytes(16)
    cipher = bytes(a ^ b for a, b in zip(data, keystream(enc_key, nonce, len(data))))
    tag = hmac.new(mac_key, nonce + cipher, hashlib.sha256).digest()
    return base64.b64encode(nonce + tag + cipher).decode()

def decrypt(token: str, enc_key, mac_key):
    raw = base64.b64decode(token)
    nonce, tag, cipher = raw[:16], raw[16:48], raw[48:]
    if not hmac.compare_digest(tag, hmac.new(mac_key, nonce + cipher, hashlib.sha256).digest()):
        raise ValueError("wrong master password or the vault was tampered with")
    return bytes(a ^ b for a, b in zip(cipher, keystream(enc_key, nonce, len(cipher))))

class Vault:
    def __init__(self, path, master):
        self.path = Path(path)
        if self.path.exists():
            meta = json.loads(self.path.read_text())
            self.salt = base64.b64decode(meta["salt"])
            self.keys = derive_keys(master, self.salt)
            self.entries = json.loads(decrypt(meta["data"], *self.keys))
        else:
            self.salt = secrets.token_bytes(16)
            self.keys = derive_keys(master, self.salt)
            self.entries = {}

    def save(self):
        data = encrypt(json.dumps(self.entries).encode(), *self.keys)
        self.path.write_text(json.dumps({"salt": base64.b64encode(self.salt).decode(), "data": data}))

    def add(self, site, user, password=None):
        password = password or "".join(secrets.choice(string.ascii_letters + string.digits + "!@#$%") for _ in range(16))
        self.entries[site] = {"user": user, "password": password}
        self.save()
        return password

if __name__ == "__main__":
    path = Path("vault_demo.json" if DEMO else "vault.json")
    master = "Correct-Horse-Battery-42" if DEMO else getpass.getpass("Master password: ")
    vault = Vault(path, master)
    if DEMO:
        print("Generated GitHub password:", vault.add("github.com", "prasanna6110"))
        vault.add("nitkkr.ac.in", "62600100", "MyCollege@2026")
        print("Vault file (encrypted):", path.read_text()[:90], "...")
        reopened = Vault(path, master)
        print("Decrypted entries:", {k: v["user"] for k, v in reopened.entries.items()})
        try:
            Vault(path, "wrong-password")
        except ValueError as e:
            print("❌", e)
        path.unlink()
    else:
        while (cmd := input("\n(a)dd (g)et (l)ist (q)uit: ").lower()) != "q":
            if cmd == "a":
                site, user = input("Site: "), input("Username: ")
                pw = input("Password (blank = generate): ")
                print("Saved. Password:", vault.add(site, user, pw or None))
            elif cmd == "g":
                e = vault.entries.get(input("Site: "))
                print(e or "Not found")
            elif cmd == "l":
                print(*vault.entries, sep="\n")
```

## Extend this project

1. Replace the cipher with `cryptography.fernet.Fernet` (`pip install cryptography`).
2. Copy a password to the clipboard and clear it after 15 seconds.
3. Warn about reused or weak passwords (reuse the strength checker project).

---

[⬅ Day 169](../Day-169-Project-Mini-Search-Engine-Inverted-Index-TF-IDF/README.md) · [🏠 Home](../README.md) · [Day 171 ➡](../Day-171-Project-Task-Scheduler-and-Reminder-Service/README.md)

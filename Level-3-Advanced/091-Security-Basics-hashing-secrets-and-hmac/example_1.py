# 091 · Security Basics: hashing, secrets and hmac — Example 1: Hashing and file integrity
# Run: python example_1.py

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

# Day 077 · Bytes, Encoding and Unicode — bytes, bytearray, hex and base64
# Run: python example_2.py

import base64

b = bytes([80, 121, 116, 104, 111, 110])
print(b, b[0], list(b))
ba = bytearray(b"hello")
ba[0] = ord("H")
ba.extend(b"!!")
print(ba, bytes(ba))
print(b"secret".hex(), bytes.fromhex("736563726574"))
enc = base64.b64encode("नमस्ते".encode())
print(enc, base64.b64decode(enc).decode())

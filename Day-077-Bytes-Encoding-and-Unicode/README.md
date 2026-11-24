# Day 077 · Bytes, Encoding and Unicode

_Intermediate_

## Text vs bytes
- `str` holds **Unicode text**, a sequence of code points like `'अ'` or `'😀'`.
- `bytes` holds **raw 8-bit data**, like `b'hello'`. Files, networks and images all work with bytes.

## Encoding and decoding
```python
"नमस्ते".encode("utf-8")   # str -> bytes
b"...".decode("utf-8")    # bytes -> str
```
- **UTF-8** is the standard: ASCII characters take 1 byte, other characters take 2 to 4 bytes.
- Error handlers: `errors="ignore" | "replace" | "strict"`.

## Other tools
- `bytearray` is the mutable version of bytes.
- `ord()`/`chr()` convert between characters and code points.
- `unicodedata` tells you character names and does normalisation.
- `base64` and `bytes.hex()` turn bytes into safe text.

## Examples

### Example 1: Encoding and decoding  ([`example_1.py`](example_1.py))

```python
text = "Hello नमस्ते 😀"
data = text.encode("utf-8")
print(data)
print("characters:", len(text), "| bytes:", len(data))
print(data.decode("utf-8"))
print("ascii with replace:", text.encode("ascii", errors="replace"))
for ch in "Aअ😀":
    print(ch, ord(ch), hex(ord(ch)), ch.encode("utf-8"))
```

### Example 2: bytes, bytearray, hex and base64  ([`example_2.py`](example_2.py))

```python
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
```

### Example 3: unicodedata and normalisation  ([`example_3.py`](example_3.py))

```python
import unicodedata

for ch in "é", "ñ", "₹", "😀":
    print(ch, unicodedata.name(ch))
s1 = "café"                       # é as one code point
s2 = "café"                 # e + combining accent
print(s1 == s2, len(s1), len(s2))
print(unicodedata.normalize("NFC", s1) == unicodedata.normalize("NFC", s2))
no_accents = "".join(c for c in unicodedata.normalize("NFD", "Crème Brûlée")
                     if unicodedata.category(c) != "Mn")
print(no_accents)
```

## Practice

1. Count the bytes and the characters in a Hindi sentence.
2. Base64-encode a small text file and decode it again.
3. Write a `slugify()` function that removes accents and replaces spaces with dashes.

---

[⬅ Day 076](../Day-076-Debugging-Techniques/README.md) · [🏠 Home](../README.md) · [Day 078 ➡](../Day-078-GUI-Programming-with-Tkinter/README.md)

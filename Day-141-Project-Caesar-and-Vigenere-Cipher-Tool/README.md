# Day 141 · Project: Caesar and Vigenère Cipher Tool

_Projects_

**Concepts:** `ord`/`chr`, the modulo operator, string building, frequency analysis (code breaking!).

Encrypt and decrypt with the Caesar and Vigenère ciphers, then **crack** a Caesar cipher automatically using English letter frequencies.

## Code

### Cipher Tool with an Automatic Cracker  ([`main.py`](main.py))

```python
import string
import sys
from collections import Counter

DEMO = not sys.stdin.isatty()
ENGLISH_FREQ = "etaoinshrdlcumwfgypbvkjxqz"

def shift_char(c, k):
    if c.isalpha():
        base = ord("A") if c.isupper() else ord("a")
        return chr((ord(c) - base + k) % 26 + base)
    return c

def caesar(text, key, decrypt=False):
    return "".join(shift_char(c, -key if decrypt else key) for c in text)

def vigenere(text, key, decrypt=False):
    out, i = [], 0
    for c in text:
        if c.isalpha():
            k = ord(key[i % len(key)].lower()) - 97
            out.append(shift_char(c, -k if decrypt else k)); i += 1
        else:
            out.append(c)
    return "".join(out)

def score_english(text):
    letters = [c for c in text.lower() if c in string.ascii_lowercase]
    common = [l for l, _ in Counter(letters).most_common(6)]
    return sum(6 - ENGLISH_FREQ.index(l) // 4 for l in common if l in ENGLISH_FREQ[:12])

def crack_caesar(cipher):
    candidates = [(score_english(caesar(cipher, k, True)), k) for k in range(26)]
    best_score, key = max(candidates)
    return key, caesar(cipher, key, True)

def main():
    msg = "Meet me at the library at seven, bring the Python notes" if DEMO else input("Message: ")
    c = caesar(msg, 7)
    v = vigenere(msg, "NITKKR")
    print("Original :", msg)
    print("Caesar+7 :", c)
    print("Decrypted:", caesar(c, 7, decrypt=True))
    print("Vigenère :", v)
    print("Decrypted:", vigenere(v, "NITKKR", decrypt=True))
    key, plain = crack_caesar(c)
    print(f"\n🕵️ Cracked the Caesar cipher without the key: key={key} -> {plain}")

if __name__ == "__main__":
    main()
```

## Extend this project

1. Add the Atbash and ROT13 ciphers.
2. Encrypt and decrypt whole text files.
3. Crack a Vigenère cipher when you know the key length (split it into Caesar columns).

---

[⬅ Day 140](../Day-140-Project-Text-Analyzer/README.md) · [🏠 Home](../README.md) · [Day 142 ➡](../Day-142-Project-Number-System-Converter/README.md)

# 068 · Bytes, Encoding and Unicode — Example 3: unicodedata and normalisation
# Run: python example_3.py

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

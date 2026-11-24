# Day 077 · Bytes, Encoding and Unicode — Encoding and decoding
# Run: python example_1.py

text = "Hello नमस्ते 😀"
data = text.encode("utf-8")
print(data)
print("characters:", len(text), "| bytes:", len(data))
print(data.decode("utf-8"))
print("ascii with replace:", text.encode("ascii", errors="replace"))
for ch in "Aअ😀":
    print(ch, ord(ch), hex(ord(ch)), ch.encode("utf-8"))

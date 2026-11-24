# Day 035 · File Handling — Binary files, seek and tell
# Run: python example_3.py

import os
path = "data.bin"
with open(path, "wb") as f:
    f.write(bytes([72, 101, 108, 108, 111]))   # "Hello"
with open(path, "rb") as f:
    print(f.read())
    f.seek(1)
    print("tell:", f.tell(), "next 3 bytes:", f.read(3))
try:
    open("does_not_exist.txt")
except FileNotFoundError as e:
    print("Handled:", e.strerror)
os.remove(path)

# 029 · File Handling — Example 1: Write, append, read
# Run: python example_1.py

import os
path = "demo_notes.txt"
with open(path, "w", encoding="utf-8") as f:
    f.write("Line 1: Python\n")
    f.write("Line 2: Files\n")
with open(path, "a", encoding="utf-8") as f:
    f.write("Line 3: Appended\n")
with open(path, encoding="utf-8") as f:
    print(f.read())
os.remove(path)    # clean up

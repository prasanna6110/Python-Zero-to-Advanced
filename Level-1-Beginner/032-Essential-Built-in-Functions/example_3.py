# 032 · Essential Built-in Functions — Example 3: chr, ord, isinstance, iter/next
# Run: python example_3.py

print(ord("A"), chr(97), [chr(c) for c in range(65, 70)])
caesar = "".join(chr((ord(c) - 97 + 3) % 26 + 97) for c in "python")
print("Caesar cipher:", caesar)
for v in [1, 2.0, "3", [4]]:
    print(v, isinstance(v, (int, float)))
it = iter([10, 20])
print(next(it), next(it), next(it, "done"))

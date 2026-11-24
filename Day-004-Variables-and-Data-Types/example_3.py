# Day 004 · Variables and Data Types — All the basic types
# Run: python example_3.py

values = [42, 3.14, 2 + 3j, "text", True, None, [1, 2], (1, 2), {"k": "v"}, {1, 2}, range(3)]
for v in values:
    print(f"{v!r:<15} -> {type(v).__name__}")

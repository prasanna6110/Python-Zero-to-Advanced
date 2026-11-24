# Day 017 · Nested Loops and Pattern Printing — Triangles and pyramids
# Run: python example_1.py

n = 5
print("Right triangle:")
for i in range(1, n + 1):
    print("* " * i)

print("\nInverted:")
for i in range(n, 0, -1):
    print("* " * i)

print("\nPyramid:")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

print("\nDiamond:")
for i in list(range(1, n + 1)) + list(range(n - 1, 0, -1)):
    print(" " * (n - i) + "* " * i)

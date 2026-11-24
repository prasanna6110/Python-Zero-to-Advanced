# Day 017 · Nested Loops and Pattern Printing — Alphabet, hollow and checkerboard patterns
# Run: python example_3.py

n = 5
print("Alphabet triangle:")
for i in range(n):
    print(" ".join(chr(65 + j) for j in range(i + 1)))

print("\nHollow square:")
for i in range(n):
    if i in (0, n - 1):
        print("* " * n)
    else:
        print("* " + "  " * (n - 2) + "*")

print("\nHollow pyramid:")
for i in range(1, n + 1):
    if i == n:
        print("*" * (2 * n - 1))
    else:
        inner = 2 * i - 3
        print(" " * (n - i) + "*" + (" " * inner + "*" if inner > 0 else ""))

print("\nCheckerboard:")
for i in range(4):
    print("".join("██" if (i + j) % 2 == 0 else "  " for j in range(8)))

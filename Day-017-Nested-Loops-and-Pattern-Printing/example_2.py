# Day 017 · Nested Loops and Pattern Printing — Number patterns
# Run: python example_2.py

n = 5
print("Number triangle:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\nFloyd's triangle:")
num = 1
for i in range(1, n + 1):
    for _ in range(i):
        print(f"{num:3}", end="")
        num += 1
    print()

print("\nPascal's triangle:")
row = [1]
for i in range(n):
    print(" " * (n - i) * 2 + "".join(f"{x:4}" for x in row))
    row = [1] + [row[k] + row[k + 1] for k in range(len(row) - 1)] + [1]

print("\nMultiplication grid:")
for i in range(1, 6):
    print("".join(f"{i * j:4}" for j in range(1, 6)))

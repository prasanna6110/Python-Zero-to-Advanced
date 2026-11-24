# Day 017 · Nested Loops and Pattern Printing

_Beginner_

## Nested loops
A loop inside another loop. For each pass of the **outer** loop, the **inner** loop runs **completely**.
```python
for row in range(3):
    for col in range(4):
        ...
```
The total number of iterations is outer × inner, so watch out for O(n²) slowness.

## How to solve any pattern question
1. The **outer loop** controls the **rows**.
2. The **inner loop or loops** control what goes in each row: spaces, then stars or numbers.
3. Work out how the row number `i` relates to the count, for example "row i has i stars" or "row i has n - i spaces".
4. Use `print(..., end="")`, then a plain `print()` to move to the next line. Or build the string: `" " * spaces + "*" * stars`.

Pattern questions come up a lot in exams and placement tests, so practise every one in this day.

## Examples

### Example 1: Triangles and pyramids  ([`example_1.py`](example_1.py))

```python
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
```

### Example 2: Number patterns  ([`example_2.py`](example_2.py))

```python
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
```

### Example 3: Alphabet, hollow and checkerboard patterns  ([`example_3.py`](example_3.py))

```python
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
```

## Practice

1. Print a butterfly pattern.
2. Print the number pyramid `1`, `121`, `12321`, `1234321`.
3. Print a hollow diamond.
4. Print a right triangle of 0s and 1s that alternate (`1`, `0 1`, `1 0 1`, ...).

---

[⬅ Day 016](../Day-016-break-continue-pass-and-loop-else/README.md) · [🏠 Home](../README.md) · [Day 018 ➡](../Day-018-Functions-Basics/README.md)

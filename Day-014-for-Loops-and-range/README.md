# Day 014 · for Loops and range()

_Beginner_

## for loop
`for item in iterable:` runs the body once for **each item** of any iterable (string, list, tuple, dict, set, range, file...).

## range(start, stop, step)
- `range(5)` gives 0, 1, 2, 3, 4
- `range(2, 10, 2)` gives 2, 4, 6, 8
- `range(10, 0, -1)` counts down
- `stop` is not included.

## Useful helpers
- `enumerate(seq, start=0)` gives you the index and the value together.
- `zip(a, b)` loops over several sequences side by side.
- `reversed(seq)` and `sorted(seq)` change the order.

Avoid writing `for i in range(len(lst))`. Use `enumerate` instead.

## Examples

### Example 1: Looping over different things  ([`example_1.py`](example_1.py))

```python
for ch in "abc":
    print(ch, end=" ")
print()
for fruit in ["apple", "mango", "kiwi"]:
    print(fruit.upper())
for i in range(1, 11, 3):
    print(i, end=" ")
print()
student = {"name": "Riya", "branch": "EE"}
for key, value in student.items():
    print(key, "=", value)
```

### Example 2: Multiplication table and patterns  ([`example_2.py`](example_2.py))

```python
n = 7
for i in range(1, 11):
    print(f"{n} x {i:2} = {n * i}")

print()
for row in range(1, 6):
    print("*" * row)
```

### Example 3: enumerate and zip  ([`example_3.py`](example_3.py))

```python
names = ["Amit", "Sara", "John"]
marks = [88, 95, 72]
for rank, name in enumerate(names, start=1):
    print(rank, name)
for name, mark in zip(names, marks):
    print(f"{name}: {mark}")
total = 0
for m in marks:
    total += m
print("Average:", total / len(marks))
```

## Practice

1. Print the sum of all even numbers from 1 to 100.
2. Print a pyramid of `*` with 5 rows.
3. Find the factorial of a number using a `for` loop.

---

[⬅ Day 013](../Day-013-match-case-Structural-Pattern-Matching/README.md) · [🏠 Home](../README.md) · [Day 015 ➡](../Day-015-while-Loops/README.md)

# Day 029 · Comprehensions: list, dict and set

_Beginner_

## List comprehension
A short, readable way to build a list:
```python
[expression for item in iterable if condition]
```
It does the same job as a `for` loop with `append`, but is shorter and usually faster.

## Other comprehensions
- Dict: `{k: v for k, v in pairs}`
- Set: `{x for x in items}`
- Generator: `(x for x in items)`. It is lazy and doesn't build a list (see Generators in Level 2).

## if/else inside a comprehension
`[x if x > 0 else 0 for x in nums]`: the if/else goes **before** the `for`.
`[x for x in nums if x > 0]`: a filter goes **after** the `for`.

Keep comprehensions simple. If one gets hard to read, use a normal loop.

## Examples

### Example 1: List comprehensions  ([`example_1.py`](example_1.py))

```python
squares = [x * x for x in range(1, 11)]
evens = [x for x in range(20) if x % 2 == 0]
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
words = ["Python", "is", "AWESOME"]
lower = [w.lower() for w in words]
print(squares, evens, labels, lower, sep="\n")
```

### Example 2: Dict and set comprehensions  ([`example_2.py`](example_2.py))

```python
names = ["asha", "ravi", "meera"]
name_len = {n: len(n) for n in names}
print(name_len)
prices = {"pen": 10, "book": 250, "bag": 900}
expensive = {k: v for k, v in prices.items() if v > 100}
print(expensive)
unique_lengths = {len(n) for n in names}
print(unique_lengths)
```

### Example 3: Nested comprehensions  ([`example_3.py`](example_3.py))

```python
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)
flat = [x for row in matrix for x in row]
print(flat)
transpose = [[row[i] for row in matrix] for i in range(3)]
print(transpose)
pairs = [(a, b) for a in "AB" for b in range(2)]
print(pairs)
```

## Practice

1. Make a list of all numbers from 1 to 100 that are divisible by both 3 and 5.
2. Build a dict mapping each number from 1 to 10 to its cube.
3. Extract all the vowels in a sentence using a set comprehension.

---

[⬅ Day 028](../Day-028-Dictionaries/README.md) · [🏠 Home](../README.md) · [Day 030 ➡](../Day-030-Classic-List-and-Dictionary-Programs/README.md)

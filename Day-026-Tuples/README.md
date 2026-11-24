# Day 026 · Tuples

_Beginner_

## Tuples
An **ordered, immutable** collection: `(1, 2, 3)`.

- A single-item tuple needs a comma: `(5,)`. Without it, `(5)` is just the number 5.
- The parentheses are optional: `t = 1, 2, 3`.
- Methods: `count()` and `index()` only.
- **Why use tuples?** They are faster and safer (they can't be changed), can be dict keys, and are good for fixed records like coordinates.
- **Unpacking**: `x, y = point` and `first, *rest = t`.

## Examples

### Example 1: Basics  ([`example_1.py`](example_1.py))

```python
t = (10, 20, 30, 20)
print(t[0], t[-1], t[1:3])
print(t.count(20), t.index(30))
single = (5,)
not_tuple = (5)
print(type(single), type(not_tuple))
# t[0] = 99 -> TypeError: tuples are immutable
```

### Example 2: Unpacking  ([`example_2.py`](example_2.py))

```python
point = (3, 4)
x, y = point
print(f"x={x}, y={y}")

first, *middle, last = (1, 2, 3, 4, 5)
print(first, middle, last)

def min_max(lst):
    return min(lst), max(lst)     # returns a tuple
lo, hi = min_max([5, 2, 9])
print(lo, hi)
```

### Example 3: Tuples as dictionary keys  ([`example_3.py`](example_3.py))

```python
distances = {
    ("Delhi", "Kurukshetra"): 160,
    ("Delhi", "Agra"): 230,
}
print(distances[("Delhi", "Agra")])

students = [("Asha", 91), ("Vikram", 85), ("Zoya", 97)]
for name, mark in sorted(students, key=lambda s: s[1], reverse=True):
    print(name, mark)
```

## Practice

1. Store 3 RGB colours as tuples and print them.
2. Swap the first and last elements of a tuple by building a new tuple.
3. Why can a tuple be a dict key while a list can't?

---

[⬅ Day 025](../Day-025-List-Methods/README.md) · [🏠 Home](../README.md) · [Day 027 ➡](../Day-027-Sets/README.md)

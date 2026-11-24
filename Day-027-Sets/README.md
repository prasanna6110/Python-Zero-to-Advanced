# Day 027 · Sets

_Beginner_

## Sets
An **unordered** collection of **unique**, hashable items: `{1, 2, 3}`.

- An empty set is `set()`. Writing `{}` creates an empty **dict**.
- Checking membership with `in` is very fast (on average it takes the same time however big the set is).
- Adding and removing: `add`, `update`, `remove` (raises an error if the item is missing), `discard` (no error), `pop`, `clear`.

## Set maths
| Operation | Operator | Method |
|-----------|----------|--------|
| Union | `a \| b` | `a.union(b)` |
| Intersection | `a & b` | `a.intersection(b)` |
| Difference | `a - b` | `a.difference(b)` |
| Symmetric difference | `a ^ b` | `a.symmetric_difference(b)` |
| Subset / superset | `a <= b` | `issubset`, `issuperset` |

A `frozenset` is an immutable set.

## Examples

### Example 1: Removing duplicates  ([`example_1.py`](example_1.py))

```python
emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com", "b@x.com"]
unique = set(emails)
print(unique, len(unique))
s = {1, 2}
s.add(3)
s.update([4, 5])
s.discard(10)       # no error
print(s)
```

### Example 2: Set operations  ([`example_2.py`](example_2.py))

```python
python_students = {"Amit", "Riya", "Karan", "Neha"}
java_students = {"Riya", "Neha", "Sam"}
print("Both:", python_students & java_students)
print("Either:", python_students | java_students)
print("Only Python:", python_students - java_students)
print("Exactly one:", python_students ^ java_students)
print({"Riya"} <= java_students)
```

### Example 3: Fast membership and frozenset  ([`example_3.py`](example_3.py))

```python
import time
big_list = list(range(1_000_000))
big_set = set(big_list)

t = time.perf_counter(); 999_999 in big_list; list_time = time.perf_counter() - t
t = time.perf_counter(); 999_999 in big_set; set_time = time.perf_counter() - t
print(f"list lookup: {list_time:.6f}s, set lookup: {set_time:.6f}s")

fs = frozenset({"read", "write"})
permissions = {fs: "editor"}       # a frozenset can be a dict key
print(permissions)
```

## Practice

1. Find the common elements of 3 lists.
2. Check whether two strings are anagrams (hint: sets alone aren't enough, so why not?).
3. Find the letters that appear in `"python"` but not in `"java"`.

---

[⬅ Day 026](../Day-026-Tuples/README.md) · [🏠 Home](../README.md) · [Day 028 ➡](../Day-028-Dictionaries/README.md)

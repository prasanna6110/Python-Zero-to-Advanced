# 054 · Advanced Sorting

## sorted() and list.sort()
- `key=` is a function that gives each item a "sort value".
- `reverse=True` sorts in descending order.
- Python's sort (**Timsort**) is **stable**: items that compare equal keep their original order. That lets you sort by several keys in multiple passes.

## Sorting by several keys
- Use a tuple as the key: `key=lambda s: (s.grade, s.name)`.
- To sort numbers in descending order inside a tuple key, negate them: `(-score, name)`.

## The operator module
`itemgetter`, `attrgetter` and `methodcaller` are faster and cleaner than lambdas.

## Custom comparison
`functools.cmp_to_key` turns an old-style `cmp(a, b)` function into a key.

## Examples

### Example 1: Keys, multiple criteria and stability  ([`example_1.py`](example_1.py))

```python
students = [("Ravi", "B", 82), ("Asha", "A", 95), ("Meera", "B", 82), ("Kiran", "A", 88)]
print(sorted(students, key=lambda s: s[2], reverse=True))
print(sorted(students, key=lambda s: (s[1], -s[2], s[0])))

# Stability: sort by the secondary key first, then by the primary key
step1 = sorted(students, key=lambda s: s[0])
step2 = sorted(step1, key=lambda s: s[1])
print(step2)
```

### Example 2: itemgetter and attrgetter  ([`example_2.py`](example_2.py))

```python
from operator import itemgetter, attrgetter
from dataclasses import dataclass

rows = [{"name": "Zed", "age": 30}, {"name": "Amy", "age": 25}, {"name": "Bob", "age": 30}]
print(sorted(rows, key=itemgetter("age", "name")))

@dataclass
class Emp:
    name: str
    salary: int

emps = [Emp("A", 300), Emp("B", 100), Emp("C", 200)]
print([e.name for e in sorted(emps, key=attrgetter("salary"))])
print(max(emps, key=attrgetter("salary")))
```

### Example 3: cmp_to_key and natural sort  ([`example_3.py`](example_3.py))

```python
from functools import cmp_to_key
import re

def largest_number(nums):
    """Arrange numbers so they form the largest possible number."""
    def cmp(a, b):
        return -1 if a + b > b + a else (1 if a + b < b + a else 0)
    return "".join(sorted(map(str, nums), key=cmp_to_key(cmp)))

print(largest_number([3, 30, 34, 5, 9]))

files = ["file10.txt", "file2.txt", "file1.txt"]
natural = lambda s: [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", s)]
print(sorted(files), "vs", sorted(files, key=natural))
```

## Practice

1. Sort products by category (A–Z), then by price (high to low).
2. Sort words by length, breaking ties alphabetically.
3. Sort a list of version strings like "1.10.0" and "1.2.5" correctly.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

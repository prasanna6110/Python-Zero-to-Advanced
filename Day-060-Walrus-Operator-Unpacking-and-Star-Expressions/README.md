# Day 060 · Walrus Operator, Unpacking and Star Expressions

_Intermediate_

## Walrus operator `:=` (Python 3.8+)
It **assigns and returns** a value inside an expression.
```python
if (n := len(data)) > 10:
    print(n)
```
It's useful in `while` loops, comprehensions and `if` checks, because you avoid computing the same thing twice.

## Extended unpacking
- `a, *b, c = [1, 2, 3, 4, 5]` gives `b = [2, 3, 4]`.
- Nested: `(a, b), c = (1, 2), 3`.
- Ignore values with `_`: `_, x, _ = t`.

## Star expressions
- Building collections: `[*a, *b]`, `{*s1, *s2}`, `{**d1, **d2}`.
- Function calls: `f(*args, **kwargs)`.
- Printing: `print(*items, sep=", ")`.

## Examples

### Example 1: Walrus operator  ([`example_1.py`](example_1.py))

```python
data = [5, 12, 7, 20, 3]
if (n := len(data)) > 3:
    print(f"List is long ({n} items)")

values = [1, 4, 9, 16, 25]
roots = [r for v in values if (r := v ** 0.5) > 2]
print(roots)

stream = iter(["a", "b", "", "c"])
while (item := next(stream)) != "":
    print("read", item)
```

### Example 2: Extended and nested unpacking  ([`example_2.py`](example_2.py))

```python
first, *middle, last = range(1, 8)
print(first, middle, last)

*_, final = "python"
print(final)

record = ("Asha", (21, "EE"), [9.1, 8.7])
name, (age, branch), [sem1, sem2] = record
print(name, age, branch, sem1, sem2)

for i, (k, v) in enumerate({"a": 1, "b": 2}.items()):
    print(i, k, v)
```

### Example 3: Star expressions for merging  ([`example_3.py`](example_3.py))

```python
a, b = [1, 2], [3, 4]
print([*a, *b, 5])
print({*"hello", *"world"})
base = {"host": "localhost", "port": 8000}
prod = {**base, "host": "example.com", "debug": False}
print(prod)
print(*["x", "y", "z"], sep=" | ")
def show(a, b, c): return a + b + c
print(show(*[1, 2], **{"c": 3}))
```

## Practice

1. Use walrus in a loop that reads "input" chunks until it gets an empty string.
2. Split a list into its head and tail using unpacking.
3. Merge three dictionaries in one line.

---

[⬅ Day 059](../Day-059-Type-Hints-Basics/README.md) · [🏠 Home](../README.md) · [Day 061 ➡](../Day-061-Advanced-Sorting/README.md)

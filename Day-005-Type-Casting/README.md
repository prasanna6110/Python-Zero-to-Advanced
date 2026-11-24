# Day 005 · Type Casting

_Beginner_

## What is type casting?
Type casting means **converting a value from one type to another**.

- **Implicit** (automatic): `5 + 2.0` gives `7.0`. Python turns the int into a float for you.
- **Explicit** (manual): you call `int()`, `float()`, `str()`, `bool()`, `list()`, `tuple()` or `set()`.

## Rules to remember
- `int("10")` works, but `int("10.5")` raises a **ValueError**. Use `int(float("10.5"))` instead.
- `int(3.99)` gives `3`, because it **cuts off** the decimal part instead of rounding.
- `bool()` is `False` for `0`, `0.0`, `""`, `[]`, `{}`, `set()` and `None`. Everything else is `True`.

## Examples

### Example 1: Implicit vs explicit conversion  ([`example_1.py`](example_1.py))

```python
a = 5          # int
b = 2.5        # float
print(a + b, type(a + b))   # implicit: int -> float

num_str = "100"
print(int(num_str) + 50)    # explicit: str -> int
print(str(50) + "%")        # explicit: int -> str
```

### Example 2: Truthy and falsy values  ([`example_2.py`](example_2.py))

```python
for value in [0, 1, -5, 0.0, "", "0", [], [0], None, {}]:
    print(f"bool({value!r}) = {bool(value)}")
```

### Example 3: Converting between collections  ([`example_3.py`](example_3.py))

```python
word = "banana"
print(list(word))
print(set(word))            # duplicates are removed
print(tuple([1, 2, 3]))
print(int("1010", 2))       # binary string -> int
print(hex(255), oct(8), bin(5))
print(float("3.14") * 2)
```

## Practice

1. Convert `"45.78"` to an int (the answer should be 45).
2. Why does `"5" + 5` fail, and how do you fix it?
3. Find the number of unique letters in `"mississippi"` using a type conversion.

---

[⬅ Day 004](../Day-004-Variables-and-Data-Types/README.md) · [🏠 Home](../README.md) · [Day 006 ➡](../Day-006-Numbers-in-Depth-int-float-Decimal-Fraction-and-complex/README.md)

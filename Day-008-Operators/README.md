# Day 008 · Operators

_Beginner_

## Types of operators
| Category | Operators |
|----------|-----------|
| Arithmetic | `+ - * / // % **` |
| Comparison | `== != > < >= <=` |
| Logical | `and or not` |
| Assignment | `= += -= *= /= //= %= **=` |
| Identity | `is`, `is not` (same object in memory?) |
| Membership | `in`, `not in` |
| Bitwise | `& \| ^ ~ << >>` |

## Precedence (highest to lowest)
`**` → unary `-` / `~` → `* / // %` → `+ -` → `<< >>` → `&` → `^` → `|` → comparisons → `not` → `and` → `or`

When in doubt, **use parentheses**.

## Important
- `==` compares **values**, while `is` compares **identity**. Use `is` only with `None`, `True` and `False`.
- `and`/`or` **short-circuit**: they stop as soon as the answer is known and return one of the operands, not always a bool.
- Comparisons can be chained: `1 < x < 10`.

## Examples

### Example 1: Arithmetic and assignment  ([`example_1.py`](example_1.py))

```python
a, b = 17, 5
print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)
print("a // b =", a // b)
print("a % b  =", a % b)
print("a ** 2 =", a ** 2)

count = 10
count += 5
count *= 2
print("count =", count)
```

### Example 2: Comparison, logical, identity, membership  ([`example_2.py`](example_2.py))

```python
x = 15
print(10 < x < 20)                 # chained comparison
print(x > 10 and x % 2 == 0)
print(not x == 15)

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b, a is b)              # same value, different objects
print(2 in a, 5 not in a)
print("" or "default")             # 'or' returns the first truthy value
```

### Example 3: Bitwise operators  ([`example_3.py`](example_3.py))

```python
a, b = 12, 10          # 1100, 1010
print(f"a & b  = {a & b}  ({a & b:04b})")
print(f"a | b  = {a | b} ({a | b:04b})")
print(f"a ^ b  = {a ^ b}  ({a ^ b:04b})")
print(f"a << 1 = {a << 1}")
print(f"a >> 2 = {a >> 2}")
n = 7
print("Is 7 odd?", bool(n & 1))   # fast odd/even check
```

## Practice

1. Check whether a year is a leap year using one expression with `and`/`or`.
2. What does `print(0 or [] or "hi" or 5)` print, and why?
3. Swap two numbers using XOR (`^`) only.

---

[⬅ Day 007](../Day-007-Taking-User-Input/README.md) · [🏠 Home](../README.md) · [Day 009 ➡](../Day-009-Strings-Basics-Indexing-and-Slicing/README.md)

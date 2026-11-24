# 009 · String Formatting

## Three ways to format
1. **f-strings** (recommended, Python 3.6+): `f"Hello {name}"`
2. **`str.format()`**: `"Hello {}".format(name)`
3. **`%` formatting** (old style): `"Hello %s" % name`

## Format specification: `{value:fill align width .precision type}`
| Spec | Meaning | Example |
|------|---------|---------|
| `.2f` | 2 decimal places | `3.14` |
| `,` | thousands separator | `1,000,000` |
| `>10` `<10` `^10` | right/left/center in width 10 | |
| `%` | percentage | `85.00%` |
| `b` `x` `o` | binary / hex / octal | |
| `e` | scientific notation | |

## Extra f-string features
- `f"{x=}"` prints `x=5`, which is handy for debugging.
- `f"{name!r}"` uses `repr()`.
- You can put any expression inside: `f"{a+b}"`, `f"{name.upper()}"`.

## Examples

### Example 1: Three ways compared  ([`example_1.py`](example_1.py))

```python
name, marks = "Neha", 92.456
print(f"{name} scored {marks:.2f}")
print("{} scored {:.2f}".format(name, marks))
print("%s scored %.2f" % (name, marks))
print("{n} scored {m:.1f}".format(n=name, m=marks))
```

### Example 2: Alignment and number formats  ([`example_2.py`](example_2.py))

```python
items = [("Pen", 10, 2), ("Notebook", 55.5, 3), ("Bag", 1299, 1)]
print(f"{'Item':<10}{'Price':>10}{'Qty':>5}")
print("-" * 25)
for item, price, qty in items:
    print(f"{item:<10}{price:>10.2f}{qty:>5}")
print(f"{1234567.891:,.2f}")
print(f"{0.8567:.2%}")
print(f"{255:b} {255:x} {255:o} {12345678:e}")
```

### Example 3: Debugging with f-strings  ([`example_3.py`](example_3.py))

```python
x, y = 10, 3
print(f"{x=}, {y=}, {x / y=:.3f}")
name = "Python"
print(f"{name!r} has {len(name)} letters, upper: {name.upper()}")
width = 12
print(f"{'center':^{width}}|")    # nested braces for a dynamic width
```

## Practice

1. Print a receipt with item names left-aligned and prices right-aligned to 2 decimals.
2. Print `0.4567` as a percentage with one decimal place.
3. Print the number 1,00,000 with comma separators using an f-string.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

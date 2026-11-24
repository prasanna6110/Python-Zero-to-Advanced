# Day 002 · print(), Comments and Escape Sequences

_Beginner_

## print() in detail
`print(*values, sep=' ', end='\n', file=sys.stdout, flush=False)`

- `sep`: what goes **between** values (a space by default).
- `end`: what goes **at the end** (a newline by default).

## Comments
- A single-line comment starts with `#`.
- For multi-line notes, use several `#` lines or a triple-quoted string. A string that is never used is ignored.
- Comments explain **why** the code does something, not **what** it does.

## Escape sequences
| Sequence | Meaning |
|----------|---------|
| `\n` | new line |
| `\t` | tab |
| `\\` | backslash |
| `\'` `\"` | quotes |

A **raw string** `r"C:\new"` turns escapes off.

## Examples

### Example 1: sep and end  ([`example_1.py`](example_1.py))

```python
print("Python", "is", "fun")
print("Python", "is", "fun", sep="-")
print("2026", "11", "24", sep="/")
print("Loading", end="...")
print("Done!")
```

### Example 2: Comments  ([`example_2.py`](example_2.py))

```python
# This is a single-line comment
price = 499       # inline comment: price in rupees

"""
This is a multi-line string.
Python ignores it because it isn't used, so
people often use it as a block comment.
"""
print("Price:", price)
```

### Example 3: Escape sequences and raw strings  ([`example_3.py`](example_3.py))

```python
print("Line 1\nLine 2")
print("Name\tMarks")
print("Ravi\t95")
print("He said \"Python is great\"")
print("Windows path: C:\\Users\\student")
print(r"Raw string: C:\new\folder")   # \n is not treated as a newline
```

## Practice

1. Print a 3-row table of names and marks using `\t`.
2. Print `a|b|c` using a single `print()` call with `sep`.
3. Print the numbers 1 to 5 on one line using `end`.

---

[⬅ Day 001](../Day-001-Introduction-to-Python/README.md) · [🏠 Home](../README.md) · [Day 003 ➡](../Day-003-Keywords-Identifiers-Indentation-and-Code-Structure/README.md)

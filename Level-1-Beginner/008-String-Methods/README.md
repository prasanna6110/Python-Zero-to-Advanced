# 008 · String Methods

## Common methods (each one returns a **new** string)
| Method | Purpose |
|--------|---------|
| `upper()`, `lower()`, `title()`, `capitalize()`, `swapcase()` | change case |
| `strip()`, `lstrip()`, `rstrip()` | remove whitespace or given characters |
| `replace(old, new)` | replace text |
| `split(sep)`, `join(iterable)` | break apart / glue together |
| `find()`, `index()`, `count()` | search |
| `startswith()`, `endswith()` | check prefix / suffix |
| `isdigit()`, `isalpha()`, `isalnum()`, `isspace()`, `isupper()` | tests |
| `center()`, `ljust()`, `rjust()`, `zfill()` | padding |
| `removeprefix()`, `removesuffix()` | Python 3.9+ |

`find()` returns `-1` when the text isn't found, while `index()` raises an error.

## Examples

### Example 1: Case and cleaning  ([`example_1.py`](example_1.py))

```python
text = "   hello PYTHON world   "
print(repr(text.strip()))
print(text.strip().title())
print(text.upper())
print(text.lower().strip().capitalize())
print("Python".swapcase())
```

### Example 2: Searching and replacing  ([`example_2.py`](example_2.py))

```python
s = "I like Java. Java is good."
print(s.find("Java"), s.find("C++"))
print(s.count("Java"))
print(s.replace("Java", "Python"))
print(s.startswith("I"), s.endswith("."))
print("report.pdf".removesuffix(".pdf"))
```

### Example 3: split, join and validation  ([`example_3.py`](example_3.py))

```python
csv_line = "Ravi,21,CSE,8.9"
parts = csv_line.split(",")
print(parts)
print(" | ".join(parts))

for value in ["12345", "abc", "abc123", "   "]:
    print(f"{value!r}: digit={value.isdigit()} alpha={value.isalpha()} alnum={value.isalnum()}")

print("7".zfill(3), "Title".center(20, "*"))
```

## Practice

1. Count the vowels in a sentence.
2. Turn `"hello world from python"` into `"Hello-World-From-Python"`.
3. Check whether a password is valid: at least 8 characters with both letters and digits.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

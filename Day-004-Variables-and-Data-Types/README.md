# Day 004 · Variables and Data Types

_Beginner_

## Variables
A variable is a **name that points to a value** in memory. You create one with `=`.

```python
age = 21
```

## Naming rules
- Names can contain letters, digits and `_`, but **cannot start with a digit**.
- Names cannot be keywords (`if`, `for`, `class`, ...).
- Convention: `snake_case` for variables and `UPPER_CASE` for constants.

## Built-in data types
| Type | Example | Category |
|------|---------|----------|
| `int` | `10` | number |
| `float` | `3.14` | number |
| `complex` | `2+3j` | number |
| `str` | `"hello"` | text |
| `bool` | `True`, `False` | boolean |
| `NoneType` | `None` | "nothing" |
| `list`, `tuple`, `range` | `[1,2]`, `(1,2)` | sequence |
| `dict` | `{"a": 1}` | mapping |
| `set`, `frozenset` | `{1,2}` | set |

Use `type(x)` to see a value's type and `id(x)` to see its memory identity.

Python is **dynamically typed**: the same variable can later hold a value of a different type.

## Examples

### Example 1: Creating variables  ([`example_1.py`](example_1.py))

```python
name = "Aarav"
age = 20
height = 5.9
is_student = True

print(name, age, height, is_student)
print(type(name), type(age), type(height), type(is_student))
```

### Example 2: Multiple assignment and swapping  ([`example_2.py`](example_2.py))

```python
a, b, c = 1, 2, 3
print(a, b, c)

x = y = z = 0          # same value to many variables
print(x, y, z)

a, b = b, a            # swap without a temporary variable
print("After swap:", a, b)
```

### Example 3: All the basic types  ([`example_3.py`](example_3.py))

```python
values = [42, 3.14, 2 + 3j, "text", True, None, [1, 2], (1, 2), {"k": "v"}, {1, 2}, range(3)]
for v in values:
    print(f"{v!r:<15} -> {type(v).__name__}")
```

## Practice

1. Create variables for your name, age, CGPA and whether you live in a hostel. Print each one with its type.
2. Swap two variables in one line.
3. Which of these names are invalid: `2name`, `_name`, `name-2`, `for`, `Name2`?

---

[⬅ Day 003](../Day-003-Keywords-Identifiers-Indentation-and-Code-Structure/README.md) · [🏠 Home](../README.md) · [Day 005 ➡](../Day-005-Type-Casting/README.md)

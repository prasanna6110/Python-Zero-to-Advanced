# 052 · Type Hints Basics

## Type hints (annotations)
They describe the **expected types** of variables, parameters and return values. Python does **not** enforce them when the code runs. Tools like **mypy**, **pyright** and your editor use them to catch bugs.

```python
def greet(name: str, times: int = 1) -> str: ...
age: int = 21
```
## Common hints (Python 3.10+ syntax)
| Hint | Meaning |
|------|---------|
| `list[int]`, `dict[str, float]`, `tuple[int, str]`, `set[str]` | collections |
| `tuple[int, ...]` | a tuple of any length |
| `int \| None` | optional value |
| `int \| str` | union |
| `Callable[[int], str]` | a function |
| `Any` | anything |

Check a file with `pip install mypy`, then `mypy file.py`.

## Examples

### Example 1: Annotating functions  ([`example_1.py`](example_1.py))

```python
def calculate_bmi(weight: float, height: float) -> float:
    return round(weight / height ** 2, 2)

def find_user(users: dict[int, str], uid: int) -> str | None:
    return users.get(uid)

print(calculate_bmi(70, 1.75))
print(find_user({1: "Asha"}, 1), find_user({1: "Asha"}, 2))
print(calculate_bmi.__annotations__)
```

### Example 2: Collections, Callable and type aliases  ([`example_2.py`](example_2.py))

```python
from collections.abc import Callable

Matrix = list[list[float]]          # type alias

def apply(func: Callable[[int], int], values: list[int]) -> list[int]:
    return [func(v) for v in values]

def identity(n: int) -> Matrix:
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

print(apply(lambda x: x * 10, [1, 2, 3]))
print(identity(3))
```

### Example 3: Hints are not enforced at runtime  ([`example_3.py`](example_3.py))

```python
def double(x: int) -> int:
    return x * 2

print(double(5))
print(double("ha"))     # works! Python doesn't check, but mypy would flag it

import typing
print(typing.get_type_hints(double))
```

## Practice

1. Add type hints to 5 functions you wrote earlier, then run mypy on them.
2. Write `merge(a: dict[str, int], b: dict[str, int]) -> dict[str, int]`.
3. What's the difference between `list[int] | None` and `list[int | None]`?

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

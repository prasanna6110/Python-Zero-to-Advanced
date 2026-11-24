# 106 · Modern Python Features (3.10 to 3.13)

## What's new, and worth knowing
| Version | Feature |
|---------|---------|
| 3.10 | `match`/`case`, the `X \| Y` union type, better error messages, `zip(strict=True)` |
| 3.11 | **10–60% faster** CPython, `ExceptionGroup` and `except*`, `add_note()`, `TaskGroup`, `asyncio.timeout`, `tomllib`, `Self`, `StrEnum` |
| 3.12 | the `type` statement and generic syntax `def f[T]()`, PEP 701 f-strings (nested quotes and multi-line), `itertools.batched`, `@override`, per-interpreter GIL |
| 3.13 | experimental **free-threading** (no GIL), an experimental JIT, a new interactive REPL (colours, multi-line editing), `copy.replace()`, `warnings.deprecated` |

## Exception groups
Raise several unrelated errors at once (common in concurrency) and handle them separately with `except*`.

## Examples

### Example 1: ExceptionGroup, except* and add_note  ([`example_1.py`](example_1.py))

```python
def validate(user):
    errors = []
    if not user.get("name"):
        errors.append(ValueError("name is required"))
    if user.get("age", 0) < 0:
        errors.append(ValueError("age must be positive"))
    if "@" not in user.get("email", ""):
        errors.append(TypeError("email is malformed"))
    if errors:
        raise ExceptionGroup("invalid user", errors)

try:
    validate({"name": "", "age": -2, "email": "nope"})
except* ValueError as eg:
    print("Value errors:", [str(e) for e in eg.exceptions])
except* TypeError as eg:
    print("Type errors:", [str(e) for e in eg.exceptions])

try:
    int("abc")
except ValueError as e:
    e.add_note("Hint: the input came from config.toml line 3")
    print(e, "| notes:", e.__notes__)
```

### Example 2: tomllib, new f-strings, batched and zip(strict)  ([`example_2.py`](example_2.py))

```python
import tomllib
from itertools import batched

config = tomllib.loads('''
[app]
name = "Course Portal"
debug = true
[database]
port = 5432
hosts = ["db1", "db2"]
''')
print(config["app"]["name"], config["database"]["hosts"])

songs = ["a", "b"]
print(f"Songs: {", ".join(songs)}")             # PEP 701: reuse the same quotes (3.12+)
print(f"{'nested ' f'{1 + 1}'}")
print(list(batched(range(7), 3)))
try:
    list(zip([1, 2, 3], ["a", "b"], strict=True))
except ValueError as e:
    print("zip strict:", e)
```

### Example 3: The type statement, @override and copy.replace  ([`example_3.py`](example_3.py))

```python
import sys
from typing import override
from dataclasses import dataclass

type Vector = list[float]
type Mapping[K, V] = dict[K, list[V]]

def scale(v: Vector, k: float) -> Vector:
    return [x * k for x in v]

class Base:
    def greet(self) -> str: return "base"

class Child(Base):
    @override                         # type checkers complain if Base has no greet()
    def greet(self) -> str: return "child"

@dataclass(frozen=True)
class Config:
    host: str
    port: int

print(scale([1.0, 2.0], 3), Vector.__value__, Child().greet())
if sys.version_info >= (3, 13):
    import copy
    print(copy.replace(Config("localhost", 80), port=443))
else:
    from dataclasses import replace
    print(replace(Config("localhost", 80), port=443))
print("Running on Python", sys.version.split()[0])
```

## Practice

1. Validate a form and report every error at once with an ExceptionGroup.
2. Load your app settings from a `pyproject.toml` with `tomllib`.
3. Try the new 3.13 REPL and the free-threaded build (`python3.13t`) if you can install them.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

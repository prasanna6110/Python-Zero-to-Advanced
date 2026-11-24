# 044 · Dataclasses

## @dataclass (Python 3.7+)
It automatically writes `__init__`, `__repr__` and `__eq__` for classes that mainly hold data.

```python
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float = 0.0
```
## Options
| Option | Effect |
|--------|--------|
| `order=True` | adds `< <= > >=` |
| `frozen=True` | immutable and hashable |
| `slots=True` | uses `__slots__`, so it takes less memory (3.10+) |
| `kw_only=True` | all fields become keyword-only (3.10+) |

- `field(default_factory=list)` gives each object its own mutable default.
- `__post_init__` lets you validate or compute fields after `__init__`.
- `asdict()`, `astuple()` and `replace()` are handy helpers.

## Examples

### Example 1: Basic dataclass  ([`example_1.py`](example_1.py))

```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    roll: int
    cgpa: float = 0.0

s1 = Student("Asha", 101, 9.1)
s2 = Student("Asha", 101, 9.1)
print(s1)                 # automatic __repr__
print(s1 == s2)           # automatic __eq__
```

### Example 2: Defaults, post_init and ordering  ([`example_2.py`](example_2.py))

```python
from dataclasses import dataclass, field

@dataclass(order=True)
class Task:
    priority: int
    title: str = field(compare=False)
    tags: list = field(default_factory=list, compare=False)

    def __post_init__(self):
        if self.priority < 0:
            raise ValueError("priority must be >= 0")
        self.title = self.title.strip().title()

tasks = [Task(3, " write report "), Task(1, "fix bug", ["urgent"]), Task(2, "review pr")]
for t in sorted(tasks):
    print(t)
```

### Example 3: Frozen dataclasses and helpers  ([`example_3.py`](example_3.py))

```python
from dataclasses import dataclass, asdict, astuple, replace

@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float

delhi = Coordinate(28.61, 77.21)
print(asdict(delhi), astuple(delhi))
moved = replace(delhi, lat=29.97)     # creates a new object
print(moved)
print({delhi: "Delhi"})               # frozen makes it hashable
try:
    delhi.lat = 0
except Exception as e:
    print(type(e).__name__, e)
```

## Practice

1. Build an `Employee` dataclass with a default salary and a `tax()` method.
2. Make an `Order` dataclass with a list of items (use `default_factory`).
3. Compare how many lines a dataclass saves over writing a normal class by hand.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

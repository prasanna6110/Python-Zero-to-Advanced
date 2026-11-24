# Day 052 · Enums

_Intermediate_

## Enum
A set of **named constants**. It is safer and more readable than "magic" strings or numbers.

```python
from enum import Enum, auto

class Color(Enum):
    RED = 1
    GREEN = 2
```
- `Color.RED.name` gives `"RED"` and `Color.RED.value` gives `1`.
- `Color(1)` gives `Color.RED`, and `Color["RED"]` also gives `Color.RED`.
- You can loop over the members: `for c in Color:`.
- `auto()` picks the values for you.
- `IntEnum` behaves like an int, `StrEnum` (3.11+) behaves like a str, and `Flag` supports bitwise combinations.
- `@unique` stops two members from having the same value.

## Examples

### Example 1: Basic Enum  ([`example_1.py`](example_1.py))

```python
from enum import Enum

class Status(Enum):
    PENDING = "pending"
    SHIPPED = "shipped"
    DELIVERED = "delivered"

order_status = Status.SHIPPED
print(order_status, order_status.name, order_status.value)
print(Status("delivered"), Status["PENDING"])
for s in Status:
    print(" -", s.name)
print(order_status == Status.SHIPPED, order_status is Status.SHIPPED)
```

### Example 2: auto, methods and match  ([`example_2.py`](example_2.py))

```python
from enum import Enum, auto

class Planet(Enum):
    MERCURY = auto()
    EARTH = auto()
    MARS = auto()

    def describe(self):
        match self:
            case Planet.EARTH:
                return "home"
            case _:
                return "far away"

for p in Planet:
    print(p.value, p.name, p.describe())
```

### Example 3: IntEnum, StrEnum and Flag  ([`example_3.py`](example_3.py))

```python
from enum import IntEnum, StrEnum, Flag, auto

class Priority(IntEnum):
    LOW = 1
    HIGH = 3

class Env(StrEnum):
    DEV = auto()
    PROD = auto()

class Perm(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()

print(Priority.HIGH > Priority.LOW, Priority.HIGH + 1)
print(Env.PROD, Env.PROD == "prod")
user = Perm.READ | Perm.WRITE
print(user, Perm.WRITE in user, Perm.EXECUTE in user)
```

## Practice

1. Create a `TrafficLight` enum with a `next()` method.
2. Use `Flag` to model file permissions (rwx).
3. Replace string status checks in an old program with an Enum.

---

[⬅ Day 051](../Day-051-Dataclasses/README.md) · [🏠 Home](../README.md) · [Day 053 ➡](../Day-053-Iterators-and-the-Iterator-Protocol/README.md)

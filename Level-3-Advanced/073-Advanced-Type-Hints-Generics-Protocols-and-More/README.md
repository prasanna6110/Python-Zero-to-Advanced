# 073 · Advanced Type Hints: Generics, Protocols and More

## Generics
Python 3.12 has new, cleaner syntax for them:
```python
def first[T](items: list[T]) -> T: ...
class Box[T]:
    def __init__(self, item: T): ...
type Pair[T] = tuple[T, T]          # type alias statement
```
The older style uses `T = TypeVar("T")` and `class Box(Generic[T])`.

## Protocol: static duck typing
```python
class Drawable(Protocol):
    def draw(self) -> str: ...
```
Any class with a matching `draw()` method satisfies it, **with no inheritance**. Add `@runtime_checkable` if you also want `isinstance` to work.

## More tools from `typing`
| Tool | Use |
|------|-----|
| `TypedDict` | dicts with known keys and their types |
| `Literal["r", "w"]` | only these exact values |
| `Final` | can't be reassigned |
| `@overload` | several signatures for one function |
| `Self` (3.11) | the current class's type |
| `ParamSpec`, `Concatenate` | typing decorators |
| `TypeGuard` / `TypeIs` | custom type-narrowing functions |
| `Annotated[int, meta]` | attach metadata (FastAPI and Pydantic use this) |
| `NewType` | a distinct type built on another, like `UserId(int)` |

## Examples

### Example 1: Generic functions and classes (3.12 syntax)  ([`example_1.py`](example_1.py))

```python
def first[T](items: list[T]) -> T:
    return items[0]

class Stack[T]:
    def __init__(self) -> None:
        self._items: list[T] = []
    def push(self, item: T) -> None:
        self._items.append(item)
    def pop(self) -> T:
        return self._items.pop()

type Pair[T] = tuple[T, T]

def swap[T](p: Pair[T]) -> Pair[T]:
    return p[1], p[0]

s: Stack[int] = Stack()
s.push(1); s.push(2)
print(first(["a", "b"]), s.pop(), swap((1, 2)))
```

### Example 2: Protocols (structural typing)  ([`example_2.py`](example_2.py))

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class SupportsArea(Protocol):
    def area(self) -> float: ...

class Square:
    def __init__(self, s: float): self.s = s
    def area(self) -> float: return self.s ** 2

class Circle:
    def __init__(self, r: float): self.r = r
    def area(self) -> float: return 3.14159 * self.r ** 2

def total_area(shapes: list[SupportsArea]) -> float:
    return sum(s.area() for s in shapes)

print(round(total_area([Square(2), Circle(1)]), 3))
print(isinstance(Square(1), SupportsArea), isinstance("text", SupportsArea))
```

### Example 3: TypedDict, Literal, overload, Self and Annotated  ([`example_3.py`](example_3.py))

```python
from typing import TypedDict, Literal, overload, Self, Annotated, NewType, Final

class Movie(TypedDict):
    title: str
    year: int

Mode = Literal["r", "w"]
UserId = NewType("UserId", int)
MAX_USERS: Final = 100

@overload
def parse(x: str) -> int: ...
@overload
def parse(x: bytes) -> str: ...
def parse(x):
    return int(x) if isinstance(x, str) else x.decode()

class Builder:
    def __init__(self) -> None: self.parts: list[str] = []
    def add(self, p: str) -> Self:
        self.parts.append(p)
        return self

Age = Annotated[int, "must be between 0 and 150"]
def set_age(a: Age) -> None: ...

m: Movie = {"title": "Inception", "year": 2010}
mode: Mode = "r"
print(m, mode, UserId(7), parse("42"), parse(b"hi"))
print(" ".join(Builder().add("a").add("b").parts))
print(set_age.__annotations__)
```

## Practice

1. Write a generic `Queue[T]` class.
2. Write a `Comparable` protocol and a generic `max_of[T: Comparable]`.
3. Run `mypy --strict` on one of your projects and fix the errors it reports.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

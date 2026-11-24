# 073 · Advanced Type Hints: Generics, Protocols and More — Example 3: TypedDict, Literal, overload, Self and Annotated
# Run: python example_3.py

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

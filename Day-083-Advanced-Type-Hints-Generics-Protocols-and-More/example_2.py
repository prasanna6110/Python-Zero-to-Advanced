# Day 083 · Advanced Type Hints: Generics, Protocols and More — Protocols (structural typing)
# Run: python example_2.py

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

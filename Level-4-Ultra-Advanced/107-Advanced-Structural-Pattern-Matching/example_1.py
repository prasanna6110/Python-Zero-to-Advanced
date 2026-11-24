# 107 · Advanced Structural Pattern Matching — Example 1: Class patterns with dataclasses
# Run: python example_1.py

from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

def where(p):
    match p:
        case Point(0, 0):
            return "origin"
        case Point(0, y):
            return f"on the Y axis at {y}"
        case Point(x, 0):
            return f"on the X axis at {x}"
        case Point(x, y) if x == y:
            return f"on the diagonal at {x}"
        case Point():
            return f"somewhere ({p.x}, {p.y})"
        case _:
            return "not a point"

for p in [Point(0, 0), Point(0, 5), Point(3, 0), Point(4, 4), Point(1, 9), "x"]:
    print(p, "->", where(p))
print(Point.__match_args__)

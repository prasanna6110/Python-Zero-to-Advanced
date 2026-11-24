# Day 047 · Polymorphism and Duck Typing — Polymorphism through overriding
# Run: python example_1.py

class Shape:
    def area(self):
        raise NotImplementedError

class Rect(Shape):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14159 * self.r ** 2

shapes = [Rect(3, 4), Circle(2), Rect(1, 1)]
for s in shapes:
    print(f"{type(s).__name__}: {s.area():.2f}")
print("Total:", round(sum(s.area() for s in shapes), 2))

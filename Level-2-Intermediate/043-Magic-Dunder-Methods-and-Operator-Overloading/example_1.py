# 043 · Magic (Dunder) Methods and Operator Overloading — Example 1: A Vector class
# Run: python example_1.py

class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, k):
        return Vector(self.x * k, self.y * k)
    __rmul__ = __mul__                    # makes 3 * v work too
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
    def __bool__(self):
        return bool(self.x or self.y)

a, b = Vector(3, 4), Vector(1, 2)
print(a + b, a - b, a * 2, 3 * b, abs(a), a == Vector(3, 4), bool(Vector(0, 0)))

# Day 046 · Encapsulation, Name Mangling and Properties — Computed and read-only properties
# Run: python example_3.py

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14159 * self.radius ** 2

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, d):
        self.radius = d / 2

c = Circle(5)
print(c.area, c.diameter)
c.diameter = 20
print(c.radius, round(c.area, 2))
try:
    c.area = 100
except AttributeError as e:
    print("Read-only:", e)

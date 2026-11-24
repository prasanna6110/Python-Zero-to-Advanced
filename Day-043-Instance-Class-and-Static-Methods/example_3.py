# Day 043 · Instance, Class and Static Methods — classmethod works with subclasses
# Run: python example_3.py

class Shape:
    @classmethod
    def create(cls):
        return cls()

    def __repr__(self):
        return f"<{type(self).__name__}>"

class Circle(Shape):
    pass

print(Shape.create(), Circle.create())   # cls is the actual class it was called on

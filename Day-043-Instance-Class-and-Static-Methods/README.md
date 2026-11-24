# Day 043 · Instance, Class and Static Methods

_Intermediate_

| Type | Decorator | First parameter | Can access |
|------|-----------|-----------------|------------|
| Instance method | (none) | `self` | the object and the class |
| Class method | `@classmethod` | `cls` | the class only |
| Static method | `@staticmethod` | (none) | nothing automatically |

## When to use each
- **Instance method**: works with the object's own data.
- **Class method**: an **alternative constructor** (`Date.from_string(...)`), or code that changes class-level state.
- **Static method**: a helper that belongs with the class logically but needs neither `self` nor `cls`.

## Examples

### Example 1: All three side by side  ([`example_1.py`](example_1.py))

```python
class Pizza:
    base_price = 200

    def __init__(self, toppings):
        self.toppings = toppings

    def price(self):                       # instance method
        return self.base_price + 50 * len(self.toppings)

    @classmethod
    def margherita(cls):                   # alternative constructor
        return cls(["cheese", "tomato"])

    @staticmethod
    def is_veg(topping):                   # helper
        return topping not in {"chicken", "pepperoni"}

p = Pizza.margherita()
print(p.toppings, p.price())
print(Pizza.is_veg("chicken"), Pizza.is_veg("olive"))
```

### Example 2: Class methods as alternative constructors  ([`example_2.py`](example_2.py))

```python
class Date:
    def __init__(self, day, month, year):
        self.day, self.month, self.year = day, month, year

    @classmethod
    def from_string(cls, text):            # "13-01-1998"
        d, m, y = map(int, text.split("-"))
        return cls(d, m, y)

    @staticmethod
    def is_leap(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def __repr__(self):
        return f"Date({self.day}, {self.month}, {self.year})"

d = Date.from_string("13-01-1998")
print(d, Date.is_leap(2024), Date.is_leap(1900))
```

### Example 3: classmethod works with subclasses  ([`example_3.py`](example_3.py))

```python
class Shape:
    @classmethod
    def create(cls):
        return cls()

    def __repr__(self):
        return f"<{type(self).__name__}>"

class Circle(Shape):
    pass

print(Shape.create(), Circle.create())   # cls is the actual class it was called on
```

## Practice

1. Add a classmethod `from_dict` to a `User` class.
2. Write a `Temperature` class with a static method that converts C to F.
3. Use a classmethod to count instances.

---

[⬅ Day 042](../Day-042-Constructors-Instance-and-Class-Attributes/README.md) · [🏠 Home](../README.md) · [Day 044 ➡](../Day-044-Inheritance/README.md)

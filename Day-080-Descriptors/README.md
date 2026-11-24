# Day 080 · Descriptors

_Advanced_

## Descriptors are the machinery behind properties, methods, classmethod and staticmethod
A descriptor is an object, stored as a **class attribute**, that defines one or more of:
- `__get__(self, obj, objtype)`
- `__set__(self, obj, value)`
- `__delete__(self, obj)`
- `__set_name__(self, owner, name)` (3.6+), which tells the descriptor its attribute name

## Two kinds
- **Data descriptor** (defines `__set__` or `__delete__`): it wins over the instance `__dict__`. `property` is one.
- **Non-data descriptor** (only `__get__`): the instance `__dict__` wins. Functions are non-data descriptors, and that's how methods get bound to `self`.

## How Python looks up `obj.attr`
1. Data descriptor on the class
2. The instance's `__dict__`
3. Non-data descriptor or plain class attribute
4. `__getattr__` (if it's defined)

**Use them for** reusable validation, typed fields (as ORMs like Django and SQLAlchemy do), lazy attributes and unit conversion.

## Examples

### Example 1: A reusable validated field  ([`example_1.py`](example_1.py))

```python
class Positive:
    def __set_name__(self, owner, name):
        self.private = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private)

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError(f"{self.private[1:]} must be positive, got {value}")
        setattr(obj, self.private, value)

class Product:
    price = Positive()
    quantity = Positive()

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

p = Product(99.5, 3)
print(p.price, p.quantity)
try:
    p.quantity = -1
except ValueError as e:
    print("Error:", e)
```

### Example 2: A typed field system (a mini ORM)  ([`example_2.py`](example_2.py))

```python
class Field:
    def __init__(self, kind, required=True):
        self.kind, self.required = kind, required
    def __set_name__(self, owner, name):
        self.name = name
    def __get__(self, obj, objtype=None):
        return self if obj is None else obj.__dict__.get(self.name)
    def __set__(self, obj, value):
        if value is None and not self.required:
            obj.__dict__[self.name] = None
            return
        if not isinstance(value, self.kind):
            raise TypeError(f"{self.name} must be {self.kind.__name__}, got {type(value).__name__}")
        obj.__dict__[self.name] = value

class User:
    name = Field(str)
    age = Field(int)
    email = Field(str, required=False)
    def __init__(self, name, age, email=None):
        self.name, self.age, self.email = name, age, email

u = User("Prasanna", 28)
print(u.name, u.age, u.email)
try:
    User("X", "twenty")
except TypeError as e:
    print("TypeError:", e)
```

### Example 3: Lazy attributes and how methods bind  ([`example_3.py`](example_3.py))

```python
class Lazy:
    """Non-data descriptor: computes once, then the instance dict takes over."""
    def __init__(self, func):
        self.func = func
    def __set_name__(self, owner, name):
        self.name = name
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        value = self.func(obj)
        obj.__dict__[self.name] = value     # later lookups skip the descriptor
        return value

class Report:
    @Lazy
    def data(self):
        print("  loading data...")
        return list(range(5))

r = Report()
print(r.data)
print(r.data)

def greet(self): return f"hi from {self}"
class A: pass
bound = greet.__get__(A(), A)          # exactly what Python does for methods
print(bound, "->", bound()[:10])
```

## Practice

1. Write a `Range(min, max)` descriptor for validating numbers.
2. Write a descriptor that logs every read and write of an attribute.
3. Explain why a property beats an instance attribute of the same name, while a function doesn't.

---

[⬅ Day 079](../Day-079-new-vs-init-and-slots/README.md) · [🏠 Home](../README.md) · [Day 081 ➡](../Day-081-Metaclasses/README.md)

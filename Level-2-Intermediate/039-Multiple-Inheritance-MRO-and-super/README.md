# 039 · Multiple Inheritance, MRO and super()

## Multiple inheritance
`class C(A, B):` means C inherits from both A and B.

## MRO (Method Resolution Order)
The order in which Python searches classes for a method. It uses the **C3 linearization** algorithm. You can see it with `Class.__mro__` or `Class.mro()`.

## The diamond problem
```
    A
   / \
  B   C
   \ /
    D
```
With the C3 MRO, D → B → C → A. **Each class appears exactly once.**

## `super()` is cooperative
`super()` means "the **next class in the MRO**", not just "the parent". For this to work, every class should call `super()`.

## Mixins
Small classes that add one feature, for example `JsonMixin` or `LogMixin`. They're a clean use of multiple inheritance.

## Examples

### Example 1: Basic multiple inheritance  ([`example_1.py`](example_1.py))

```python
class Flyer:
    def fly(self):
        return "flying"

class Swimmer:
    def swim(self):
        return "swimming"

class Duck(Flyer, Swimmer):
    pass

d = Duck()
print(d.fly(), d.swim())
print([c.__name__ for c in Duck.__mro__])
```

### Example 2: Diamond and cooperative super()  ([`example_2.py`](example_2.py))

```python
class A:
    def hello(self):
        print("A")

class B(A):
    def hello(self):
        print("B"); super().hello()

class C(A):
    def hello(self):
        print("C"); super().hello()

class D(B, C):
    def hello(self):
        print("D"); super().hello()

D().hello()          # D B C A: each class runs once
print([k.__name__ for k in D.mro()])
```

### Example 3: Mixins  ([`example_3.py`](example_3.py))

```python
import json

class JsonMixin:
    def to_json(self):
        return json.dumps(self.__dict__)

class ReprMixin:
    def __repr__(self):
        fields = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{type(self).__name__}({fields})"

class Product(JsonMixin, ReprMixin):
    def __init__(self, name, price):
        self.name, self.price = name, price

p = Product("Laptop", 55000)
print(p)
print(p.to_json())
```

## Practice

1. Predict the MRO of `class X(B, C)` where both B and C inherit from A.
2. Write a `TimestampMixin` that adds a `created_at` attribute.
3. What happens if B in the diamond doesn't call `super()`?

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

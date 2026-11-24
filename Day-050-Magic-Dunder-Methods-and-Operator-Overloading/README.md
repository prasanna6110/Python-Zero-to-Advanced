# Day 050 · Magic (Dunder) Methods and Operator Overloading

_Intermediate_

## Dunder methods (`__double_underscore__`)
Python calls these special methods behind the scenes. Defining them makes your class behave like a built-in type.

| Category | Methods |
|----------|---------|
| Text | `__str__` (for users), `__repr__` (for developers) |
| Arithmetic | `__add__ __sub__ __mul__ __truediv__ __floordiv__ __mod__ __pow__`, plus `__radd__`... and `__iadd__`... |
| Comparison | `__eq__ __ne__ __lt__ __le__ __gt__ __ge__` |
| Container | `__len__ __getitem__ __setitem__ __delitem__ __contains__ __iter__` |
| Callable | `__call__` |
| Truthiness | `__bool__` |
| Hashing | `__hash__` (needed to use objects in sets or as dict keys) |
| Lifecycle | `__new__ __init__ __del__` |
| Context | `__enter__ __exit__` |

Return `NotImplemented` from a binary operator when you can't handle the other type. Python will then try the reflected method (for example `__radd__`).

## Examples

### Example 1: A Vector class  ([`example_1.py`](example_1.py))

```python
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
```

### Example 2: __str__ vs __repr__ and comparisons  ([`example_2.py`](example_2.py))

```python
from functools import total_ordering

@total_ordering
class Money:
    def __init__(self, amount):
        self.amount = amount
    def __repr__(self):
        return f"Money({self.amount!r})"
    def __str__(self):
        return f"₹{self.amount:,.2f}"
    def __eq__(self, other):
        return self.amount == other.amount
    def __lt__(self, other):
        return self.amount < other.amount

m = Money(1500)
print(str(m), repr(m))
print([Money(5), Money(1)])          # lists use repr
print(sorted([Money(30), Money(10), Money(20)]))
print(Money(5) >= Money(3))          # filled in by total_ordering
```

### Example 3: Container and callable behaviour  ([`example_3.py`](example_3.py))

```python
class Inventory:
    def __init__(self):
        self._items = {}
    def __setitem__(self, k, v): self._items[k] = v
    def __getitem__(self, k): return self._items[k]
    def __delitem__(self, k): del self._items[k]
    def __contains__(self, k): return k in self._items
    def __len__(self): return len(self._items)
    def __iter__(self): return iter(self._items)

class Multiplier:
    def __init__(self, n): self.n = n
    def __call__(self, x): return x * self.n

inv = Inventory()
inv["apple"] = 50
inv["mango"] = 20
del inv["apple"]
print(len(inv), "mango" in inv, inv["mango"], list(inv))
triple = Multiplier(3)
print(triple(7), callable(triple))
```

## Practice

1. Build a `Fraction` class with `+`, `*`, `==` and `__str__` (reduce fractions using the GCD).
2. Build a `Matrix` class that supports `@` through `__matmul__`.
3. Make a class hashable so its objects can go in a set.

---

[⬅ Day 049](../Day-049-Abstract-Classes-and-Interfaces-abc/README.md) · [🏠 Home](../README.md) · [Day 051 ➡](../Day-051-Dataclasses/README.md)

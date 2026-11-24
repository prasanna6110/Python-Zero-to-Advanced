# Day 049 · Abstract Classes and Interfaces (abc)

_Intermediate_

## Abstract Base Classes
An **abstract class** can't be instantiated. It defines a contract that subclasses **must** fulfil.

```python
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount): ...
```
- A subclass that doesn't implement **every** abstract method can't be instantiated either.
- An abstract class can also contain concrete (normal) methods.
- You can also make abstract properties, classmethods and staticmethods.

The `collections.abc` module provides ready-made ABCs: `Iterable`, `Sequence`, `Mapping`...

## Examples

### Example 1: Defining an interface  ([`example_1.py`](example_1.py))

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        ...

    def receipt(self, amount):           # concrete method
        return f"Receipt: ₹{amount} via {type(self).__name__}"

class UPI(Payment):
    def pay(self, amount):
        return f"Paid ₹{amount} with UPI"

class Card(Payment):
    def pay(self, amount):
        return f"Paid ₹{amount} with card"

for method in [UPI(), Card()]:
    print(method.pay(500), "|", method.receipt(500))
```

### Example 2: You cannot instantiate an incomplete class  ([`example_2.py`](example_2.py))

```python
from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def save(self, data): ...
    @abstractmethod
    def load(self): ...

class HalfDone(Storage):
    def save(self, data):
        self.data = data

for cls in [Storage, HalfDone]:
    try:
        cls()
    except TypeError as e:
        print(f"{cls.__name__}: {e}")
```

### Example 3: Using collections.abc  ([`example_3.py`](example_3.py))

```python
from collections.abc import Sequence, Iterable, Mapping

class Countdown(Sequence):           # implement 2 methods, get many for free
    def __init__(self, n): self.n = n
    def __len__(self): return self.n
    def __getitem__(self, i):
        if i >= self.n: raise IndexError
        return self.n - i

c = Countdown(5)
print(list(c), c.index(3), c.count(1), 2 in c, list(reversed(c)))
print(isinstance([1], Iterable), isinstance({}, Mapping), isinstance("x", Sequence))
```

## Practice

1. Create an abstract `Vehicle` with `start()` and `stop()`, then implement two vehicles.
2. Add an abstract property `wheels`.
3. Implement a `Mapping` subclass that reads from an environment-like dict.

---

[⬅ Day 048](../Day-048-Composition-Aggregation-and-Object-Relationships/README.md) · [🏠 Home](../README.md) · [Day 050 ➡](../Day-050-Magic-Dunder-Methods-and-Operator-Overloading/README.md)

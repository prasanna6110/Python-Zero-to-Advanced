# 042 · Abstract Classes and Interfaces (abc) — Example 3: Using collections.abc
# Run: python example_3.py

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

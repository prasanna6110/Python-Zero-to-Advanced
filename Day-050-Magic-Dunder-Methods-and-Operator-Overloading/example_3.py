# Day 050 · Magic (Dunder) Methods and Operator Overloading — Container and callable behaviour
# Run: python example_3.py

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

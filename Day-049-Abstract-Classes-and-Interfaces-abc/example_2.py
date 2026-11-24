# Day 049 · Abstract Classes and Interfaces (abc) — You cannot instantiate an incomplete class
# Run: python example_2.py

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

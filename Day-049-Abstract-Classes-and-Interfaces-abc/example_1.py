# Day 049 · Abstract Classes and Interfaces (abc) — Defining an interface
# Run: python example_1.py

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

# 043 · Magic (Dunder) Methods and Operator Overloading — Example 2: __str__ vs __repr__ and comparisons
# Run: python example_2.py

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

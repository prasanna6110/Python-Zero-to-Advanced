# Day 032 · Docstrings and PEP 8 (Writing Clean Code) — Module and class docstrings with help()
# Run: python example_3.py

class BankAccount:
    """A simple bank account.

    Attributes:
        owner: name of the account holder
        balance: current balance in rupees
    """

    def deposit(self, amount):
        """Add amount to the balance."""

print(BankAccount.__doc__)
print(BankAccount.deposit.__doc__)
import math
print(math.sqrt.__doc__)

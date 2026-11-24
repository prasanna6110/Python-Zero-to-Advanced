# 028 · Raising Exceptions and Custom Exceptions — Example 2: Custom exception classes
# Run: python example_2.py

class BankError(Exception):
    """Base class for bank errors."""

class InsufficientFundsError(BankError):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Need ₹{amount - balance} more (balance ₹{balance})")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    withdraw(500, 800)
except BankError as e:
    print("Bank error:", e, "| shortfall:", e.amount - e.balance)

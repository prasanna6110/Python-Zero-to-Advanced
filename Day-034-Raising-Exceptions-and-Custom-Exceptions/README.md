# Day 034 · Raising Exceptions and Custom Exceptions

_Beginner_

## raise
Use `raise ValueError("message")` to signal an error yourself.
Inside an `except` block, a bare `raise` re-raises the current exception.

## Custom exceptions
Create your own by inheriting from `Exception`:
```python
class InsufficientFundsError(Exception):
    pass
```
## Exception chaining
`raise NewError("...") from original_error` keeps the original cause, which makes debugging easier.

## assert
`assert condition, "message"` is a debugging check. It is **disabled** when Python runs with `-O`, so don't use it to validate user input.

## Examples

### Example 1: raise for validation  ([`example_1.py`](example_1.py))

```python
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("age must be an integer")
    if age < 0 or age > 150:
        raise ValueError(f"invalid age: {age}")
    return age

for value in [25, -5, "twenty"]:
    try:
        print("OK:", set_age(value))
    except (TypeError, ValueError) as e:
        print("Error:", e)
```

### Example 2: Custom exception classes  ([`example_2.py`](example_2.py))

```python
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
```

### Example 3: Re-raising and chaining  ([`example_3.py`](example_3.py))

```python
def load_config(text):
    try:
        key, value = text.split("=")
    except ValueError as e:
        raise RuntimeError(f"bad config line: {text!r}") from e
    return {key: value}

try:
    load_config("no-equals-sign")
except RuntimeError as e:
    print("Error:", e)
    print("Caused by:", repr(e.__cause__))
```

## Practice

1. Create `InvalidEmailError` and raise it when an email has no `@`.
2. Build an exception hierarchy for a library system.
3. What is the difference between `raise X from e` and plain `raise X`?

---

[⬅ Day 033](../Day-033-Exception-Handling-try-except-else-finally/README.md) · [🏠 Home](../README.md) · [Day 035 ➡](../Day-035-File-Handling/README.md)

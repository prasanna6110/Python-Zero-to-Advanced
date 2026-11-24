# 026 · Docstrings and PEP 8 (Writing Clean Code)

## Docstrings
A string written as the **first statement** of a module, function or class. It describes what the code does and you can read it with `help()` or `obj.__doc__`.

```python
def area(r):
    """Return the area of a circle with radius r.

    Args:
        r (float): radius
    Returns:
        float: area
    """
```

## PEP 8: the official style guide
- Indent with 4 spaces. Keep lines at 79–99 characters at most.
- Use `snake_case` for functions and variables, `PascalCase` for classes and `UPPER_CASE` for constants.
- Put 2 blank lines between top-level functions and classes.
- Put spaces around operators: `x = a + b`.
- Write imports at the top: standard library, then third-party, then your own modules.
- Tools: **black** (formatter), **ruff** or **flake8** (linters).

## Examples

### Example 1: Writing and reading docstrings  ([`example_1.py`](example_1.py))

```python
def bmi(weight_kg, height_m):
    """Calculate Body Mass Index.

    Args:
        weight_kg: weight in kilograms
        height_m: height in metres

    Returns:
        BMI rounded to 1 decimal place.
    """
    return round(weight_kg / height_m ** 2, 1)

print(bmi(70, 1.75))
print(bmi.__doc__)
```

### Example 2: Bad style vs PEP 8 style  ([`example_2.py`](example_2.py))

```python
# Bad:
def CalcTotal(L):
  t=0
  for i in L:t+=i
  return t

# Good (PEP 8):
TAX_RATE = 0.18


def calculate_total(prices):
    """Return the total of prices including tax."""
    subtotal = sum(prices)
    return subtotal * (1 + TAX_RATE)


print(CalcTotal([1, 2]), calculate_total([100, 200]))
```

### Example 3: Module and class docstrings with help()  ([`example_3.py`](example_3.py))

```python
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
```

## Practice

1. Add proper docstrings to 3 functions you wrote earlier.
2. Install `black` (`pip install black`) and format one of your files.
3. List 5 PEP 8 rules from memory.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

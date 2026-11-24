# Day 012 · Conditional Statements: if, elif, else

_Beginner_

## Syntax
```python
if condition:
    ...
elif other_condition:
    ...
else:
    ...
```
- The body **must be indented**.
- `elif` and `else` are optional, and you can have as many `elif`s as you need.
- Conditions use truthiness: `if my_list:` means "if the list is not empty".

## Ternary (conditional expression)
`result = "Even" if n % 2 == 0 else "Odd"`

## Nested conditions
You can put an `if` inside another `if`, but deep nesting is hard to read. Prefer `and`/`or` or **early returns**.

## Examples

### Example 1: Grade calculator  ([`example_1.py`](example_1.py))

```python
marks = 78
if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "Fail"
print(f"Marks: {marks}, Grade: {grade}")
```

### Example 2: Ternary and truthiness  ([`example_2.py`](example_2.py))

```python
n = 7
print("Even" if n % 2 == 0 else "Odd")

cart = []
if not cart:
    print("Your cart is empty")

username = ""
display = username or "Guest"
print("Welcome,", display)
```

### Example 3: Nested conditions: ticket price  ([`example_3.py`](example_3.py))

```python
age = 25
is_student = True
day = "Sunday"

if age < 5:
    price = 0
elif age < 18:
    price = 100
else:
    price = 200
    if is_student:
        price -= 50
if day in ("Saturday", "Sunday"):
    price += 30
print("Ticket price:", price)
```

## Practice

1. Find the largest of three numbers using `if/elif/else`.
2. Check whether a year is a leap year.
3. Electricity bill: the first 100 units cost ₹5 each, the next 100 cost ₹7 each and anything above that costs ₹10 each. Calculate the bill.

---

[⬅ Day 011](../Day-011-String-Formatting/README.md) · [🏠 Home](../README.md) · [Day 013 ➡](../Day-013-match-case-Structural-Pattern-Matching/README.md)

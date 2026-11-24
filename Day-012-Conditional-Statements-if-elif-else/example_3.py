# Day 012 · Conditional Statements: if, elif, else — Nested conditions: ticket price
# Run: python example_3.py

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

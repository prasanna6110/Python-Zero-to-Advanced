# Day 012 · Conditional Statements: if, elif, else — Ternary and truthiness
# Run: python example_2.py

n = 7
print("Even" if n % 2 == 0 else "Odd")

cart = []
if not cart:
    print("Your cart is empty")

username = ""
display = username or "Guest"
print("Welcome,", display)

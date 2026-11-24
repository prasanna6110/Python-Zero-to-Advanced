# 009 · String Formatting — Example 2: Alignment and number formats
# Run: python example_2.py

items = [("Pen", 10, 2), ("Notebook", 55.5, 3), ("Bag", 1299, 1)]
print(f"{'Item':<10}{'Price':>10}{'Qty':>5}")
print("-" * 25)
for item, price, qty in items:
    print(f"{item:<10}{price:>10.2f}{qty:>5}")
print(f"{1234567.891:,.2f}")
print(f"{0.8567:.2%}")
print(f"{255:b} {255:x} {255:o} {12345678:e}")

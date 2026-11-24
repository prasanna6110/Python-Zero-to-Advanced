# Day 003 · Keywords, Identifiers, Indentation and Code Structure — Indentation defines blocks
# Run: python example_2.py

marks = 72
if marks >= 40:
    print("Passed")          # inside the if block (4 spaces)
    if marks >= 70:
        print("Distinction")  # nested block (8 spaces)
print("This line always runs")   # back at the top level

total = (10 + 20 +
         30 + 40)            # a line can continue inside brackets
items = [
    "pen",
    "book",
]
print(total, items)

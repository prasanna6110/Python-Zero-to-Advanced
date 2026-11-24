# 012 · for Loops and range() — Example 2: Multiplication table and patterns
# Run: python example_2.py

n = 7
for i in range(1, 11):
    print(f"{n} x {i:2} = {n * i}")

print()
for row in range(1, 6):
    print("*" * row)

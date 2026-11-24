# Day 014 · for Loops and range() — enumerate and zip
# Run: python example_3.py

names = ["Amit", "Sara", "John"]
marks = [88, 95, 72]
for rank, name in enumerate(names, start=1):
    print(rank, name)
for name, mark in zip(names, marks):
    print(f"{name}: {mark}")
total = 0
for m in marks:
    total += m
print("Average:", total / len(marks))

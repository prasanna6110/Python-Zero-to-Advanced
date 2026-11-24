# 024 · Comprehensions: list, dict and set — Example 1: List comprehensions
# Run: python example_1.py

squares = [x * x for x in range(1, 11)]
evens = [x for x in range(20) if x % 2 == 0]
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
words = ["Python", "is", "AWESOME"]
lower = [w.lower() for w in words]
print(squares, evens, labels, lower, sep="\n")

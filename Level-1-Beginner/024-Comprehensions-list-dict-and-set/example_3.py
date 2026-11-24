# 024 · Comprehensions: list, dict and set — Example 3: Nested comprehensions
# Run: python example_3.py

matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)
flat = [x for row in matrix for x in row]
print(flat)
transpose = [[row[i] for row in matrix] for i in range(3)]
print(transpose)
pairs = [(a, b) for a in "AB" for b in range(2)]
print(pairs)

# Day 024 · Lists — Nested lists (matrix)
# Run: python example_2.py

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print("Middle:", matrix[1][1])
for row in matrix:
    print(" ".join(str(x) for x in row))
diagonal = [matrix[i][i] for i in range(3)]
print("Diagonal:", diagonal)

# Day 030 · Classic List and Dictionary Programs — Matrix operations without libraries
# Run: python example_2.py

A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]

def transpose(M):
    return [list(row) for row in zip(*M)]

def multiply(X, Y):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*Y)] for row in X]

def add(X, Y):
    return [[a + b for a, b in zip(r1, r2)] for r1, r2 in zip(X, Y)]

def show(M, name):
    print(name)
    for row in M:
        print("  ", " ".join(f"{v:4}" for v in row))

show(transpose(A), "Transpose of A:")
show(multiply(A, B), "A x B:")
show(add(A, A), "A + A:")

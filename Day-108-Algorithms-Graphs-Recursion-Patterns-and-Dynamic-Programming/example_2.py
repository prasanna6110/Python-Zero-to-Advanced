# Day 108 · Algorithms: Graphs, Recursion Patterns and Dynamic Programming — Backtracking: permutations and N-Queens
# Run: python example_2.py

def permutations(items):
    result, path, used = [], [], [False] * len(items)
    def backtrack():
        if len(path) == len(items):
            result.append(path[:]); return
        for i, x in enumerate(items):
            if not used[i]:
                used[i] = True; path.append(x)
                backtrack()
                path.pop(); used[i] = False
    backtrack()
    return result

def n_queens(n):
    solutions, cols, d1, d2, board = [], set(), set(), set(), []
    def place(r):
        if r == n:
            solutions.append(board[:]); return
        for c in range(n):
            if c in cols or r - c in d1 or r + c in d2: continue
            cols.add(c); d1.add(r - c); d2.add(r + c); board.append(c)
            place(r + 1)
            cols.remove(c); d1.remove(r - c); d2.remove(r + c); board.pop()
    place(0)
    return solutions

print(permutations([1, 2, 3]))
sols = n_queens(6)
print(f"6-Queens has {len(sols)} solutions. First one:")
for c in sols[0]:
    print(" ".join("Q" if i == c else "." for i in range(6)))

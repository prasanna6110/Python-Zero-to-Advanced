# Day 158 · Project: Sudoku Solver and Generator — Sudoku Solver and Generator
# Run: python main.py

import random
import sys
import time

DEMO = not sys.stdin.isatty()
PUZZLE = """
53..7....
6..195...
.98....6.
8...6...3
4..8.3..1
7...2...6
.6....28.
...419..5
....8..79
"""

def parse(text):
    return [[int(c) if c.isdigit() else 0 for c in row.strip()] for row in text.strip().splitlines()]

def show(b):
    for r in range(9):
        if r % 3 == 0:
            print("+-------+-------+-------+")
        print("| " + " | ".join(" ".join(str(b[r][c]) if b[r][c] else "." for c in range(i, i + 3)) for i in (0, 3, 6)) + " |")
    print("+-------+-------+-------+")

def candidates(b, r, c):
    used = set(b[r]) | {b[i][c] for i in range(9)} | {b[i][j] for i in range(r // 3 * 3, r // 3 * 3 + 3)
                                                     for j in range(c // 3 * 3, c // 3 * 3 + 3)}
    return [n for n in range(1, 10) if n not in used]

def solve(b, count_only=False, limit=2):
    empties = [(r, c) for r in range(9) for c in range(9) if b[r][c] == 0]
    if not empties:
        return 1
    r, c = min(empties, key=lambda rc: len(candidates(b, *rc)))   # most constrained cell first
    total = 0
    for n in candidates(b, r, c):
        b[r][c] = n
        total += solve(b, count_only, limit)
        if total and not count_only:
            return total
        if total >= limit:
            break
        b[r][c] = 0
    if count_only:
        b[r][c] = 0
    return total

def generate(clues=30):
    board = [[0] * 9 for _ in range(9)]
    for i in range(0, 9, 3):                                          # fill the diagonal boxes randomly
        nums = random.sample(range(1, 10), 9)
        for k in range(9):
            board[i + k // 3][i + k % 3] = nums[k]
    solve(board)
    cells = random.sample(range(81), 81)
    for idx in cells:
        r, c = divmod(idx, 9)
        if sum(v != 0 for row in board for v in row) <= clues:
            break
        backup, board[r][c] = board[r][c], 0
        if solve([row[:] for row in board], count_only=True) != 1:
            board[r][c] = backup                                      # keep the solution unique
    return board

if __name__ == "__main__":
    board = parse(PUZZLE)
    if not DEMO and input("Enter your own puzzle? (y/n) ") == "y":
        print("Enter 9 rows, using . for empty cells:")
        board = parse("\n".join(input(f"row {i + 1}: ") for i in range(9)))
    print("🧩 Puzzle:"); show(board)
    t = time.perf_counter()
    print("Unique solution:", solve([row[:] for row in board], count_only=True) == 1)
    solve(board)
    print(f"✅ Solved in {time.perf_counter() - t:.3f}s:"); show(board)
    if DEMO:
        random.seed(10)
    print("\n🎲 A newly generated puzzle:"); show(generate())

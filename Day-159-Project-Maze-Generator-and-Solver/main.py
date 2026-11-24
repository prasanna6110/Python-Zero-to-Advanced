# Day 159 · Project: Maze Generator and Solver — Maze Generator and Solver (BFS vs A*)
# Run: python main.py

import heapq
import random
import sys
from collections import deque

DEMO = not sys.stdin.isatty()

def generate(w, h):
    grid = [["█"] * (2 * w + 1) for _ in range(2 * h + 1)]
    stack, seen = [(0, 0)], {(0, 0)}
    grid[1][1] = " "
    while stack:
        x, y = stack[-1]
        nbrs = [(x + dx, y + dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
                if 0 <= x + dx < w and 0 <= y + dy < h and (x + dx, y + dy) not in seen]
        if not nbrs:
            stack.pop(); continue
        nx, ny = random.choice(nbrs)
        grid[2 * y + 1 + (ny - y)][2 * x + 1 + (nx - x)] = " "       # knock down the wall
        grid[2 * ny + 1][2 * nx + 1] = " "
        seen.add((nx, ny)); stack.append((nx, ny))
    return grid

def neighbours(grid, r, c):
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if grid[r + dr][c + dc] != "█":
            yield r + dr, c + dc

def bfs(grid, start, goal):
    q, parent = deque([start]), {start: None}
    while q:
        cur = q.popleft()
        if cur == goal:
            break
        for n in neighbours(grid, *cur):
            if n not in parent:
                parent[n] = cur; q.append(n)
    return parent

def astar(grid, start, goal):
    h = lambda p: abs(p[0] - goal[0]) + abs(p[1] - goal[1])
    pq, parent, g = [(h(start), start)], {start: None}, {start: 0}
    while pq:
        _, cur = heapq.heappop(pq)
        if cur == goal:
            break
        for n in neighbours(grid, *cur):
            if n not in g or g[cur] + 1 < g[n]:
                g[n] = g[cur] + 1; parent[n] = cur
                heapq.heappush(pq, (g[n] + h(n), n))
    return parent

def path_from(parent, goal):
    path = []
    while goal:
        path.append(goal); goal = parent[goal]
    return path[::-1]

def main(w=18, h=8):
    grid = generate(w, h)
    start, goal = (1, 1), (2 * h - 1, 2 * w - 1)
    for name, algo in [("BFS", bfs), ("A*", astar)]:
        parent = algo(grid, start, goal)
        path = path_from(parent, goal)
        print(f"{name}: path length {len(path)}, explored {len(parent)} cells")
    for r, c in path:
        grid[r][c] = "•"
    grid[start[0]][start[1]], grid[goal[0]][goal[1]] = "S", "E"
    print("\n".join("".join(row) for row in grid))

if __name__ == "__main__":
    if DEMO:
        random.seed(21)
        main()
    else:
        main(int(input("Width (e.g. 20): ") or 20), int(input("Height (e.g. 10): ") or 10))

# Day 108 · Algorithms: Graphs, Recursion Patterns and Dynamic Programming

_Advanced_

## Graphs
Store a graph as an **adjacency list**: `{node: [neighbours]}`.
| Algorithm | Use |
|-----------|-----|
| BFS (with a queue) | shortest path in an **unweighted** graph, level order |
| DFS (with a stack or recursion) | connectivity, cycles, topological sort |
| Dijkstra (with a heap) | shortest path with **weighted** edges (no negative weights) |
| Topological sort | ordering tasks that depend on each other |

## Backtracking
Try a choice → recurse → undo the choice. Used for permutations, N-Queens and Sudoku.

## Dynamic Programming
Use it when a problem has **overlapping subproblems** and **optimal substructure**.
- **Top-down**: recursion plus memoization (`@cache`).
- **Bottom-up**: fill in a table.

Classic DP problems: Fibonacci, the 0/1 knapsack, LCS, coin change and edit distance.

## Examples

### Example 1: BFS, DFS and Dijkstra  ([`example_1.py`](example_1.py))

```python
from collections import deque
import heapq

graph = {"A": ["B", "C"], "B": ["D"], "C": ["D", "E"], "D": ["F"], "E": ["F"], "F": []}

def bfs_path(g, start, goal):
    q, parent = deque([start]), {start: None}
    while q:
        node = q.popleft()
        if node == goal:
            path = []
            while node: path.append(node); node = parent[node]
            return path[::-1]
        for nb in g[node]:
            if nb not in parent:
                parent[nb] = node; q.append(nb)

def dfs(g, node, seen=None):
    seen = seen if seen is not None else []
    seen.append(node)
    for nb in g[node]:
        if nb not in seen: dfs(g, nb, seen)
    return seen

roads = {"Delhi": {"Panipat": 90, "Ambala": 200}, "Panipat": {"Kurukshetra": 75},
         "Ambala": {"Kurukshetra": 40}, "Kurukshetra": {}}
def dijkstra(g, src):
    dist, pq = {src: 0}, [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist.get(u, float("inf")): continue
        for v, w in g[u].items():
            if d + w < dist.get(v, float("inf")):
                dist[v] = d + w; heapq.heappush(pq, (dist[v], v))
    return dist

print("BFS shortest A->F:", bfs_path(graph, "A", "F"))
print("DFS order:", dfs(graph, "A"))
print("Dijkstra from Delhi:", dijkstra(roads, "Delhi"))
```

### Example 2: Backtracking: permutations and N-Queens  ([`example_2.py`](example_2.py))

```python
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
```

### Example 3: Dynamic programming classics  ([`example_3.py`](example_3.py))

```python
from functools import cache

def coin_change(coins, amount):
    dp = [0] + [float("inf")] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1

def knapsack(items, capacity):          # items: (weight, value)
    dp = [0] * (capacity + 1)
    for w, v in items:
        for c in range(capacity, w - 1, -1):
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[capacity]

def lcs(a, b):
    @cache
    def go(i, j):
        if i == len(a) or j == len(b): return ""
        if a[i] == b[j]: return a[i] + go(i + 1, j + 1)
        return max(go(i + 1, j), go(i, j + 1), key=len)
    return go(0, 0)

def edit_distance(s, t):
    dp = list(range(len(t) + 1))
    for i in range(1, len(s) + 1):
        prev, dp[0] = dp[0], i
        for j in range(1, len(t) + 1):
            prev, dp[j] = dp[j], min(dp[j] + 1, dp[j - 1] + 1, prev + (s[i - 1] != t[j - 1]))
    return dp[-1]

print("coins for ₹11 with [1,2,5]:", coin_change([1, 2, 5], 11))
print("knapsack:", knapsack([(1, 1), (3, 4), (4, 5), (5, 7)], 7))
print("LCS:", lcs("AGGTAB", "GXTXAYB"))
print("edit distance kitten->sitting:", edit_distance("kitten", "sitting"))
```

## Practice

1. Detect a cycle in a directed graph using DFS.
2. Solve the "climbing stairs" problem (1 or 2 steps at a time) with DP.
3. Write a Sudoku solver using backtracking.

---

[⬅ Day 107](../Day-107-Algorithms-Searching-and-Sorting/README.md) · [🏠 Home](../README.md) · [Day 109 ➡](../Day-109-Generator-Internals-send-throw-close-and-yield-from/README.md)

# Day 108 · Algorithms: Graphs, Recursion Patterns and Dynamic Programming — BFS, DFS and Dijkstra
# Run: python example_1.py

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

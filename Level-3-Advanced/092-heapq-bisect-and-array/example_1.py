# 092 · heapq, bisect and array — Example 1: Priority queue with heapq
# Run: python example_1.py

import heapq
from itertools import count

tasks = []
c = count()
for priority, task in [(3, "write docs"), (1, "fix prod bug"), (2, "code review"), (1, "reply to client")]:
    heapq.heappush(tasks, (priority, next(c), task))

while tasks:
    p, _, task = heapq.heappop(tasks)
    print(f"[P{p}] {task}")

scores = [88, 42, 99, 73, 65, 91]
print("top 3:", heapq.nlargest(3, scores), "bottom 2:", heapq.nsmallest(2, scores))

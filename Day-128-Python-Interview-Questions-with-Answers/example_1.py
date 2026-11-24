# Day 128 · Python Interview Questions (with Answers) — Proving the basics in code
# Run: python example_1.py

import copy

a = [1, [2, 3]]
shallow, deep = copy.copy(a), copy.deepcopy(a)
a[1].append(4)
print("shallow shares nested:", shallow, "| deep is independent:", deep)

x = [1, 2]; y = [1, 2]
print("x == y:", x == y, "| x is y:", x is y)

lst = [1, 2]
lst.append([3, 4]); print("append:", lst)
lst = [1, 2]
lst.extend([3, 4]); print("extend:", lst)
lst.remove(3); print("remove(3):", lst, "| pop():", lst.pop(), "->", lst)

t = (1, 2)
try:
    t[0] = 5
except TypeError as e:
    print("tuple is immutable:", e)
print("hashable tuple as key:", {(1, 2): "ok"})

# Day 090 · Memory Management, Garbage Collection and weakref — Reference counting
# Run: python example_1.py

import sys

data = [1, 2, 3]
print("refcount:", sys.getrefcount(data))
alias = data
container = [data, data]
print("after 3 more refs:", sys.getrefcount(data))
del alias
container.clear()
print("after removing them:", sys.getrefcount(data))

a, b = 256, 256
c, d = int("257"), int("257")
print(a is b, c is d, "<- small int cache (implementation detail)")

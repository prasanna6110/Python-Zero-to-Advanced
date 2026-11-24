# Day 079 · __new__ vs __init__ and __slots__ — __slots__ saves memory
# Run: python example_3.py

import sys, tracemalloc

class Normal:
    def __init__(self, x, y): self.x, self.y = x, y

class Slotted:
    __slots__ = ("x", "y")
    def __init__(self, x, y): self.x, self.y = x, y

for cls in (Normal, Slotted):
    tracemalloc.start()
    objs = [cls(i, i) for i in range(100_000)]
    current, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"{cls.__name__:<8} {current / 1024 / 1024:.1f} MB for 100k objects")

s = Slotted(1, 2)
try:
    s.z = 3
except AttributeError as e:
    print("AttributeError:", e)

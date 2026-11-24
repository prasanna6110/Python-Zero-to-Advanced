# Day 128 · Python Interview Questions (with Answers) — Proving the advanced answers
# Run: python example_3.py

import sys, threading, time, timeit

class Slot:
    __slots__ = ("a",)
try:
    s = Slot(); s.b = 1
except AttributeError as e:
    print("__slots__:", e)

print("metaclass of int:", type(int), "| of type:", type(type))
print("refcount of a new list:", sys.getrefcount([]))

d = {i: i for i in range(100_000)}
l = list(range(100_000))
print("dict lookup :", round(timeit.timeit(lambda: 99_999 in d, number=1000), 5), "s")
print("list lookup :", round(timeit.timeit(lambda: 99_999 in l, number=1000), 5), "s")

def io(): time.sleep(0.2)
t = time.perf_counter()
ts = [threading.Thread(target=io) for _ in range(5)]
[x.start() for x in ts]; [x.join() for x in ts]
print(f"5 I/O tasks in threads: {time.perf_counter() - t:.2f}s (the GIL is released while waiting)")
print("__name__ here is:", __name__)

# Day 093 · Performance: Profiling and Optimisation — timeit micro-benchmarks
# Run: python example_1.py

import timeit

setup = "data = list(range(10_000)); s = set(data)"
print("list lookup :", timeit.timeit("9999 in data", setup, number=2000))
print("set lookup  :", timeit.timeit("9999 in s", setup, number=2000))
print("loop append :", timeit.timeit("r=[]\nfor x in range(1000): r.append(x*2)", number=2000))
print("comprehension:", timeit.timeit("[x*2 for x in range(1000)]", number=2000))
print("+= strings  :", timeit.timeit("s=''\nfor i in range(1000): s += str(i)", number=500))
print("join        :", timeit.timeit("''.join(str(i) for i in range(1000))", number=500))

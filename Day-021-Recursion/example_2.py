# Day 021 · Recursion — Fibonacci: naive vs memoized
# Run: python example_2.py

from functools import lru_cache

calls = 0
def fib_naive(n):
    global calls
    calls += 1
    return n if n < 2 else fib_naive(n - 1) + fib_naive(n - 2)

@lru_cache(maxsize=None)
def fib_fast(n):
    return n if n < 2 else fib_fast(n - 1) + fib_fast(n - 2)

print(fib_naive(20), "calls:", calls)
print(fib_fast(100))

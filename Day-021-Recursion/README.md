# Day 021 · Recursion

_Beginner_

## What is recursion?
A function that **calls itself**. Every recursive function needs:
1. A **base case**: when to stop.
2. A **recursive case**: a call on a **smaller** problem.

## Notes
- Python's default recursion limit is about 1000 calls (`sys.getrecursionlimit()`).
- Recursion is elegant for trees, divide-and-conquer and backtracking.
- A naive recursive solution can be slow (look at fibonacci). Memoization fixes this (see `functools.lru_cache`).

## Examples

### Example 1: Factorial and sum of digits  ([`example_1.py`](example_1.py))

```python
def factorial(n):
    if n <= 1:          # base case
        return 1
    return n * factorial(n - 1)

def digit_sum(n):
    return n if n < 10 else n % 10 + digit_sum(n // 10)

print(factorial(5), factorial(10))
print(digit_sum(98765))
```

### Example 2: Fibonacci: naive vs memoized  ([`example_2.py`](example_2.py))

```python
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
```

### Example 3: Recursion on nested data  ([`example_3.py`](example_3.py))

```python
def flatten(items):
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def hanoi(n, src="A", dst="C", via="B"):
    if n == 0:
        return
    hanoi(n - 1, src, via, dst)
    print(f"Move disk {n} {src} -> {dst}")
    hanoi(n - 1, via, dst, src)

print(flatten([1, [2, [3, [4, 5]], 6], 7]))
hanoi(3)
```

## Practice

1. Write a recursive `power(a, b)`.
2. Reverse a string using recursion.
3. Write recursive binary search.

---

[⬅ Day 020](../Day-020-Scope-LEGB-global-and-nonlocal/README.md) · [🏠 Home](../README.md) · [Day 022 ➡](../Day-022-Classic-Number-Programs-Exam-and-Interview-Favourites/README.md)

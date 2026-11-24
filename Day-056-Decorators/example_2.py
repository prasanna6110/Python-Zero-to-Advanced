# Day 056 · Decorators — A timing decorator
# Run: python example_2.py

import functools, time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.4f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(i * i for i in range(n))

print(slow_sum(1_000_000))

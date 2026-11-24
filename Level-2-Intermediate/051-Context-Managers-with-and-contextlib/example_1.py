# 051 · Context Managers (with and contextlib) — Example 1: A class-based context manager
# Run: python example_1.py

import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"Block took {self.elapsed:.4f}s")
        if exc_type:
            print("An error happened:", exc)
        return False        # don't suppress the error

with Timer() as t:
    total = sum(range(1_000_000))
print("total:", total)

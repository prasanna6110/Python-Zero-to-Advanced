# 063 · functools — Example 1: partial and lru_cache
# Run: python example_1.py

from functools import partial, lru_cache
import time

def power(base, exp):
    return base ** exp
square = partial(power, exp=2)
cube = partial(power, exp=3)
print(square(9), cube(3))
int_from_binary = partial(int, base=2)
print(int_from_binary("1111"))

@lru_cache(maxsize=128)
def slow_square(n):
    time.sleep(0.2)
    return n * n

t = time.perf_counter(); slow_square(12); first = time.perf_counter() - t
t = time.perf_counter(); slow_square(12); second = time.perf_counter() - t
print(f"first {first:.3f}s, cached {second:.6f}s", slow_square.cache_info())

# Day 072 · functools

_Intermediate_

## Higher-order function tools
| Tool | What it does |
|------|--------------|
| `partial(func, *args)` | "freezes" some arguments |
| `lru_cache(maxsize)` / `cache` | memoization |
| `cached_property` | a property computed once, then stored |
| `reduce` | folds an iterable into one value |
| `wraps` | for decorators |
| `total_ordering` | fills in comparison methods |
| `singledispatch` | **function overloading by type** |
| `singledispatchmethod` | the same, for methods |
| `cmp_to_key` | old-style comparison → key |

## Examples

### Example 1: partial and lru_cache  ([`example_1.py`](example_1.py))

```python
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
```

### Example 2: cached_property  ([`example_2.py`](example_2.py))

```python
from functools import cached_property

class Dataset:
    def __init__(self, numbers):
        self.numbers = numbers

    @cached_property
    def stats(self):
        print("  ...computing stats (only once)")
        n = len(self.numbers)
        mean = sum(self.numbers) / n
        var = sum((x - mean) ** 2 for x in self.numbers) / n
        return {"mean": mean, "std": var ** 0.5}

d = Dataset([2, 4, 4, 4, 5, 5, 7, 9])
print(d.stats)
print(d.stats)
```

### Example 3: singledispatch: overloading by type  ([`example_3.py`](example_3.py))

```python
from functools import singledispatch

@singledispatch
def describe(obj):
    return f"Something: {obj!r}"

@describe.register
def _(obj: int):
    return f"Integer with {len(str(abs(obj)))} digits"

@describe.register
def _(obj: list):
    return f"List of {len(obj)} items"

@describe.register(str)
def _(obj):
    return f"String of length {len(obj)}"

for item in [42, "hello", [1, 2, 3], 3.14]:
    print(describe(item))
```

## Practice

1. Use `partial` to make `log_error = partial(log, level="ERROR")`.
2. Memoize a recursive function that counts grid paths.
3. Use `singledispatch` to serialise different types into strings.

---

[⬅ Day 071](../Day-071-itertools/README.md) · [🏠 Home](../README.md) · [Day 073 ➡](../Day-073-Logging/README.md)

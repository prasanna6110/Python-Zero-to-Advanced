# 083 · Performance: Profiling and Optimisation

## Rule #1: measure, don't guess
> "Premature optimisation is the root of all evil."

## Tools
| Tool | Measures |
|------|----------|
| `time.perf_counter()` | quick timing |
| `timeit` | accurate micro-benchmarks |
| `cProfile` + `pstats` | which functions take the time |
| `tracemalloc` | memory allocations |
| `line_profiler`, `py-spy`, `scalene` | third-party, in more detail |

## Common speed-ups
1. Pick a **better algorithm or data structure** (a set or dict instead of a list for lookups). This matters most.
2. Use built-ins and the standard library (`sum`, `sorted`, `collections`): they run in C.
3. Use comprehensions and generators instead of manual loops with `append`.
4. Use `str.join` instead of `+=` in a loop.
5. Cache results (`lru_cache`).
6. Vectorise with NumPy. Use multiprocessing for CPU-heavy work.
7. Use PyPy, Cython or Numba for hot loops.

## Examples

### Example 1: timeit micro-benchmarks  ([`example_1.py`](example_1.py))

```python
import timeit

setup = "data = list(range(10_000)); s = set(data)"
print("list lookup :", timeit.timeit("9999 in data", setup, number=2000))
print("set lookup  :", timeit.timeit("9999 in s", setup, number=2000))
print("loop append :", timeit.timeit("r=[]\nfor x in range(1000): r.append(x*2)", number=2000))
print("comprehension:", timeit.timeit("[x*2 for x in range(1000)]", number=2000))
print("+= strings  :", timeit.timeit("s=''\nfor i in range(1000): s += str(i)", number=500))
print("join        :", timeit.timeit("''.join(str(i) for i in range(1000))", number=500))
```

### Example 2: cProfile to find the bottleneck  ([`example_2.py`](example_2.py))

```python
import cProfile, pstats, io

def slow_unique(items):
    result = []
    for x in items:
        if x not in result:         # O(n) check -> O(n²) overall
            result.append(x)
    return result

def fast_unique(items):
    return list(dict.fromkeys(items))

def main():
    data = list(range(3000)) * 2
    slow_unique(data)
    fast_unique(data)

pr = cProfile.Profile()
pr.enable(); main(); pr.disable()
out = io.StringIO()
pstats.Stats(pr, stream=out).sort_stats("cumulative").print_stats(5)
print("\n".join(out.getvalue().splitlines()[:18]))
```

### Example 3: tracemalloc for memory  ([`example_3.py`](example_3.py))

```python
import tracemalloc

tracemalloc.start()
big_list = [str(i) * 10 for i in range(100_000)]
gen_total = sum(len(str(i) * 10) for i in range(100_000))
snapshot = tracemalloc.take_snapshot()
current, peak = tracemalloc.get_traced_memory()
print(f"current={current / 1e6:.1f} MB peak={peak / 1e6:.1f} MB")
for stat in snapshot.statistics("lineno")[:3]:
    print(stat)
tracemalloc.stop()
```

## Practice

1. Profile one of your older programs and find its slowest function.
2. Speed up a function that finds duplicate pairs from O(n²) to O(n).
3. Measure the memory of a list vs a generator for 10 million numbers.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

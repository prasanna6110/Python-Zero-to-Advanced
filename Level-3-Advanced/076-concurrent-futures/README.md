# 076 · concurrent.futures

## A high-level, unified API for threads and processes
```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

with ThreadPoolExecutor(max_workers=5) as ex:
    futures = [ex.submit(fn, arg) for arg in args]
    for f in as_completed(futures):
        print(f.result())
```
- `ex.map(fn, items)` returns results **in the same order** as the inputs.
- `ex.submit(fn, ...)` returns a **Future**, which has `.result(timeout)`, `.done()`, `.exception()`, `.cancel()` and `.add_done_callback()`.
- `as_completed(futures)` yields futures **as they finish**.
- `wait(futures, return_when=FIRST_COMPLETED)`

Switching between threads and processes means changing just **one word**.

## Examples

### Example 1: ThreadPoolExecutor.map  ([`example_1.py`](example_1.py))

```python
from concurrent.futures import ThreadPoolExecutor
import time

def fetch(url):
    time.sleep(0.5)
    return f"{url} -> 200 OK"

urls = [f"https://site{i}.com" for i in range(6)]
start = time.perf_counter()
with ThreadPoolExecutor(max_workers=6) as ex:
    for result in ex.map(fetch, urls):
        print(result)
print(f"took {time.perf_counter() - start:.2f}s (not 3s)")
```

### Example 2: submit, as_completed and exceptions  ([`example_2.py`](example_2.py))

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time, random

random.seed(3)
def task(n):
    time.sleep(random.uniform(0.1, 0.5))
    if n == 3:
        raise ValueError("task 3 failed")
    return n * n

with ThreadPoolExecutor(4) as ex:
    futures = {ex.submit(task, n): n for n in range(6)}
    for fut in as_completed(futures):
        n = futures[fut]
        try:
            print(f"task {n} finished -> {fut.result()}")
        except ValueError as e:
            print(f"task {n} raised: {e}")
```

### Example 3: ProcessPoolExecutor for CPU work  ([`example_3.py`](example_3.py))

```python
from concurrent.futures import ProcessPoolExecutor
import math, time

def heavy(n):
    return sum(math.sqrt(i) for i in range(n))

if __name__ == "__main__":
    nums = [3_000_000] * 4
    start = time.perf_counter()
    with ProcessPoolExecutor() as ex:
        results = list(ex.map(heavy, nums))
    print([round(r) for r in results])
    print(f"process pool: {time.perf_counter() - start:.2f}s")
```

## Practice

1. Check the status of 20 (fake) websites concurrently and print each result as it arrives.
2. Add a timeout to `future.result()` and handle `TimeoutError`.
3. Benchmark a Thread pool against a Process pool on a CPU task.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

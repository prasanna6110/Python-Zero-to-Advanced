# 075 · Multiprocessing

## Processes
Every process has its **own Python interpreter and its own memory**, so it's **not limited by the GIL**. This is how you get real parallelism for **CPU-bound** work (maths, image processing, data crunching).

## API
- `multiprocessing.Process(target=f, args=())`
- `multiprocessing.Pool(n).map(f, items)`: a pool of worker processes
- Sharing data: `Queue`, `Pipe`, `Value`, `Array`, `Manager()`

## Important
- Always protect the entry point with `if __name__ == "__main__":`. On Windows and macOS, new processes **re-import** your script.
- The arguments and return values you pass are **pickled** (serialised), so they must be picklable. A lambda can't be sent to `Pool.map`.
- Starting processes is costly. Use processes for **big chunks** of work, not tiny tasks.

## Examples

### Example 1: CPU-bound: sequential vs process pool  ([`example_1.py`](example_1.py))

```python
import time
from multiprocessing import Pool, cpu_count

def count_primes(limit):
    count = 0
    for n in range(2, limit):
        if all(n % d for d in range(2, int(n ** 0.5) + 1)):
            count += 1
    return count

if __name__ == "__main__":
    jobs = [60_000] * 4
    start = time.perf_counter()
    seq = [count_primes(j) for j in jobs]
    t_seq = time.perf_counter() - start

    start = time.perf_counter()
    with Pool(min(4, cpu_count())) as pool:
        par = pool.map(count_primes, jobs)
    t_par = time.perf_counter() - start
    print(f"sequential {t_seq:.2f}s | pool {t_par:.2f}s | same result: {seq == par}")
    print("CPU cores:", cpu_count())
```

### Example 2: Process, Queue and the separate memory  ([`example_2.py`](example_2.py))

```python
from multiprocessing import Process, Queue
import os

data = []

def worker(q, n):
    data.append(n)                           # only changes the CHILD's copy
    q.put((os.getpid(), n * n))

if __name__ == "__main__":
    q = Queue()
    procs = [Process(target=worker, args=(q, i)) for i in range(4)]
    for p in procs: p.start()
    results = [q.get() for _ in procs]
    for p in procs: p.join()
    print("results:", sorted(r[1] for r in results))
    print("distinct PIDs:", len({r[0] for r in results}), "| main pid:", os.getpid())
    print("parent's data list is still:", data)
```

### Example 3: Shared Value, Array and Manager  ([`example_3.py`](example_3.py))

```python
from multiprocessing import Process, Value, Array, Manager, Lock

def add(counter, arr, shared, lock, i):
    with lock:
        counter.value += 1
    arr[i] = i * 10
    shared[f"worker{i}"] = "done"

if __name__ == "__main__":
    counter = Value("i", 0)
    arr = Array("i", 4)
    lock = Lock()
    with Manager() as m:
        shared = m.dict()
        ps = [Process(target=add, args=(counter, arr, shared, lock, i)) for i in range(4)]
        for p in ps: p.start()
        for p in ps: p.join()
        print(counter.value, list(arr), dict(sorted(shared.items())))
```

## Practice

1. Resize (simulate) 100 images in parallel with `Pool.map`.
2. Compare threads and processes on the same CPU-bound task.
3. Use `pool.imap_unordered` to show results as soon as each one finishes.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

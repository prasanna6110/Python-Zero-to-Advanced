# Day 089 · The GIL and Choosing the Right Concurrency Model

_Advanced_

## What is the GIL?
The **Global Interpreter Lock** is a lock inside CPython that lets **only one thread run Python bytecode at a time**. It keeps memory management (reference counting) simple and safe.

- The GIL is **released** while a thread waits on I/O, sleeps, or runs many C extensions (NumPy, hashlib, zlib...).
- Python 3.13 added an experimental **free-threaded build** with no GIL (`python3.13t`, PEP 703).

## Decision guide
| Workload | Best tool |
|----------|-----------|
| Lots of network or file waiting, thousands of connections | **asyncio** |
| Some I/O waiting, or blocking libraries | **threads** (`ThreadPoolExecutor`) |
| Heavy CPU computation in pure Python | **processes** (`ProcessPoolExecutor`) |
| Number crunching | **NumPy** / vectorised code (releases the GIL) |

**Concurrency** means dealing with many things at once. **Parallelism** means doing many things at the same instant.

## Examples

### Example 1: Threads do NOT speed up CPU-bound work  ([`example_1.py`](example_1.py))

```python
import threading, time

def cpu_work(n=3_000_000):
    total = 0
    for i in range(n):
        total += i * i
    return total

start = time.perf_counter()
cpu_work(); cpu_work()
seq = time.perf_counter() - start

start = time.perf_counter()
ts = [threading.Thread(target=cpu_work) for _ in range(2)]
for t in ts: t.start()
for t in ts: t.join()
thr = time.perf_counter() - start
print(f"sequential {seq:.2f}s vs 2 threads {thr:.2f}s -> the GIL stops a speed-up")
```

### Example 2: Comparing all three on an I/O task  ([`example_2.py`](example_2.py))

```python
import asyncio, threading, time
from concurrent.futures import ThreadPoolExecutor

N, DELAY = 20, 0.2

def io_task(_):
    time.sleep(DELAY)

async def aio_task():
    await asyncio.sleep(DELAY)

t = time.perf_counter()
for i in range(N): io_task(i)
print(f"sequential : {time.perf_counter() - t:.2f}s")

t = time.perf_counter()
with ThreadPoolExecutor(N) as ex: list(ex.map(io_task, range(N)))
print(f"threads    : {time.perf_counter() - t:.2f}s")

async def main(): await asyncio.gather(*(aio_task() for _ in range(N)))
t = time.perf_counter(); asyncio.run(main())
print(f"asyncio    : {time.perf_counter() - t:.2f}s")
```

### Example 3: Inspecting the interpreter's GIL situation  ([`example_3.py`](example_3.py))

```python
import sys, sysconfig

print("Python:", sys.version.split()[0])
gil_disabled_build = bool(sysconfig.get_config_var("Py_GIL_DISABLED"))
print("Free-threaded build:", gil_disabled_build)
if hasattr(sys, "_is_gil_enabled"):
    print("GIL currently enabled:", sys._is_gil_enabled())
print("Thread switch interval (s):", sys.getswitchinterval())
```

## Practice

1. Run Example 1 with processes and compare the timings.
2. Write down which model you'd pick for: a chat server, video encoding, scraping 1000 pages.
3. Read about PEP 703 (free-threaded Python) and summarise it.

---

[⬅ Day 088](../Day-088-asyncio-Advanced-Tasks-Timeouts-Queues-and-Semaphores/README.md) · [🏠 Home](../README.md) · [Day 090 ➡](../Day-090-Memory-Management-Garbage-Collection-and-weakref/README.md)

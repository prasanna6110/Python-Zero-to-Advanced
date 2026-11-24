# Day 084 · Threading

_Advanced_

## Threads
Several threads run **inside one process** and **share memory**.

- Because of the **GIL**, only one thread runs Python bytecode at a time. So threads speed up **I/O-bound** work (networks, files, sleeping) but **not** CPU-bound work.
- `threading.Thread(target=f, args=(...))`, then `.start()` and `.join()`.
- **Daemon threads** are killed automatically when the main program exits.

## Synchronisation (shared data needs protecting!)
| Tool | Use |
|------|-----|
| `Lock` / `RLock` | lets only one thread into a critical section at a time |
| `Semaphore(n)` | lets at most n threads in at once |
| `Event` | one thread signals others |
| `Condition` | wait until a condition is true |
| `queue.Queue` | a **thread-safe** producer–consumer queue (the best choice) |
| `threading.local()` | data that is private to each thread |

A **race condition** happens when the result depends on the order in which threads happen to run.

## Examples

### Example 1: I/O-bound speed-up with threads  ([`example_1.py`](example_1.py))

```python
import threading, time

def download(name, seconds):
    time.sleep(seconds)            # simulates waiting on the network
    print(f"  downloaded {name}")

files = [("a.zip", 1), ("b.zip", 1), ("c.zip", 1)]

start = time.perf_counter()
for f in files:
    download(*f)
print(f"Sequential: {time.perf_counter() - start:.2f}s")

start = time.perf_counter()
threads = [threading.Thread(target=download, args=f) for f in files]
for t in threads: t.start()
for t in threads: t.join()
print(f"Threaded:   {time.perf_counter() - start:.2f}s")
```

### Example 2: Race condition and Lock  ([`example_2.py`](example_2.py))

```python
import threading

counter = 0
lock = threading.Lock()

def unsafe(n):
    global counter
    for _ in range(n):
        tmp = counter          # read
        tmp += 1               # modify
        counter = tmp          # write (another thread may have run in between!)

def safe(n):
    global counter
    for _ in range(n):
        with lock:
            counter += 1

for worker in (unsafe, safe):
    counter = 0
    ts = [threading.Thread(target=worker, args=(200_000,)) for _ in range(4)]
    for t in ts: t.start()
    for t in ts: t.join()
    print(f"{worker.__name__}: {counter} (expected 800000)")
```

### Example 3: Producer-consumer with queue.Queue  ([`example_3.py`](example_3.py))

```python
import threading, queue, time, random

q = queue.Queue(maxsize=5)
random.seed(1)

def producer():
    for i in range(6):
        item = f"order-{i}"
        q.put(item)
        print(f"produced {item}")
        time.sleep(random.uniform(0.01, 0.05))
    q.put(None)                     # sentinel: tells the consumer to stop

def consumer():
    while (item := q.get()) is not None:
        print(f"        consumed {item}")
        time.sleep(random.uniform(0.02, 0.06))
        q.task_done()

p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)
p.start(); c.start(); p.join(); c.join()
print("All orders processed")
```

## Practice

1. Download 10 (simulated) URLs using 3 threads and a Queue.
2. Use a `Semaphore` to limit concurrent "database connections" to 2.
3. Use an `Event` to stop a background worker thread cleanly.

---

[⬅ Day 083](../Day-083-Advanced-Type-Hints-Generics-Protocols-and-More/README.md) · [🏠 Home](../README.md) · [Day 085 ➡](../Day-085-Multiprocessing/README.md)

# Day 088 · asyncio Advanced: Tasks, Timeouts, Queues and Semaphores

_Advanced_

## Managing many tasks
| Tool | Use |
|------|-----|
| `asyncio.TaskGroup()` (3.11+) | structured concurrency: if one task fails, the rest are cancelled |
| `asyncio.timeout(sec)` (3.11+) / `wait_for` | stop a task that takes too long |
| `asyncio.Semaphore(n)` | limit concurrency (for example, at most 5 requests at once) |
| `asyncio.Queue` | producer–consumer between coroutines |
| `asyncio.Lock`, `Event`, `Condition` | synchronisation |
| `asyncio.as_completed` | handle results as they arrive |
| `task.cancel()` | raises `CancelledError` inside the task |
| `gather(..., return_exceptions=True)` | collect errors instead of failing |

## Examples

### Example 1: Semaphore limiting concurrency  ([`example_1.py`](example_1.py))

```python
import asyncio, time

sem = asyncio.Semaphore(2)

async def call_api(i):
    async with sem:
        print(f"  start request {i}")
        await asyncio.sleep(0.5)
        print(f"  end   request {i}")
        return i

async def main():
    start = time.perf_counter()
    results = await asyncio.gather(*(call_api(i) for i in range(6)))
    print(results, f"{time.perf_counter() - start:.1f}s (6 requests, 2 at a time)")

asyncio.run(main())
```

### Example 2: Timeouts, cancellation and TaskGroup  ([`example_2.py`](example_2.py))

```python
import asyncio

async def slow():
    try:
        await asyncio.sleep(10)
    except asyncio.CancelledError:
        print("  slow() was cancelled, cleaning up")
        raise

async def boom():
    await asyncio.sleep(0.1)
    raise ValueError("boom!")

async def main():
    try:
        async with asyncio.timeout(0.3):
            await slow()
    except TimeoutError:
        print("Timed out!")

    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(slow())
            tg.create_task(boom())
    except* ValueError as eg:
        print("TaskGroup failed:", [str(e) for e in eg.exceptions])

    results = await asyncio.gather(boom(), asyncio.sleep(0, "ok"), return_exceptions=True)
    print(results)

asyncio.run(main())
```

### Example 3: Async producer-consumer with workers  ([`example_3.py`](example_3.py))

```python
import asyncio, random

async def producer(q, n):
    for i in range(n):
        await q.put(f"job-{i}")
    print("producer done")

async def worker(name, q, results):
    while True:
        job = await q.get()
        await asyncio.sleep(random.uniform(0.05, 0.2))
        results.append((name, job))
        q.task_done()

async def main():
    random.seed(0)
    q, results = asyncio.Queue(), []
    workers = [asyncio.create_task(worker(f"W{i}", q, results)) for i in range(3)]
    await producer(q, 9)
    await q.join()                 # wait until every job is done
    for w in workers:
        w.cancel()
    await asyncio.gather(*workers, return_exceptions=True)
    for name, job in results:
        print(name, job)

asyncio.run(main())
```

## Practice

1. Build an async "web crawler" that crawls at most 3 pages at a time (simulated).
2. Add retries with exponential backoff to an async function.
3. Use `asyncio.as_completed` to print the fastest response first.

---

[⬅ Day 087](../Day-087-asyncio-Basics/README.md) · [🏠 Home](../README.md) · [Day 089 ➡](../Day-089-The-GIL-and-Choosing-the-Right-Concurrency-Model/README.md)

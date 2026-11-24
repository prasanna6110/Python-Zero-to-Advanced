# 077 · asyncio Basics

## Asynchronous programming
**One thread** handles **thousands** of I/O tasks by switching between them while they wait. It's ideal for web servers, scrapers, chat apps and API clients.

## Key words
- `async def`: defines a **coroutine function**. Calling it gives you a coroutine object, which doesn't run yet.
- `await`: pauses this coroutine until the awaited thing finishes, letting other tasks run meanwhile.
- **Event loop**: the scheduler that runs coroutines.
- `asyncio.run(main())`: the entry point.
- `asyncio.create_task(coro)`: schedules a coroutine to run concurrently.
- `asyncio.gather(*coros)`: runs many and collects their results.

## ⚠️ Golden rules
- Never call blocking code (`time.sleep`, `requests.get`) inside async code. Use `await asyncio.sleep` and async libraries (`aiohttp`, `httpx`).
- If you must call a blocking function, use `await asyncio.to_thread(blocking_fn)`.

## Examples

### Example 1: Your first coroutine  ([`example_1.py`](example_1.py))

```python
import asyncio

async def greet(name, delay):
    print(f"Hello {name} (waiting {delay}s)")
    await asyncio.sleep(delay)
    print(f"Goodbye {name}")
    return name.upper()

async def main():
    result = await greet("Asha", 0.5)
    print("Result:", result)

coro = greet("test", 0)
print(type(coro))
coro.close()                  # creating a coroutine doesn't run it
asyncio.run(main())
```

### Example 2: Concurrency with gather and create_task  ([`example_2.py`](example_2.py))

```python
import asyncio, time

async def fetch(site, delay):
    await asyncio.sleep(delay)
    return f"{site}: {delay}s"

async def main():
    start = time.perf_counter()
    results = await asyncio.gather(fetch("A", 1), fetch("B", 1), fetch("C", 1))
    print(results, f"in {time.perf_counter() - start:.2f}s")

    t1 = asyncio.create_task(fetch("X", 0.5))
    t2 = asyncio.create_task(fetch("Y", 0.3))
    print("tasks started, doing other work...")
    print(await t1, await t2)

asyncio.run(main())
```

### Example 3: Blocking vs non-blocking and to_thread  ([`example_3.py`](example_3.py))

```python
import asyncio, time

def blocking_io():
    time.sleep(1)                 # a legacy blocking call
    return "blocking done"

async def ticker():
    for i in range(3):
        print("  tick", i)
        await asyncio.sleep(0.3)

async def main():
    start = time.perf_counter()
    result, _ = await asyncio.gather(asyncio.to_thread(blocking_io), ticker())
    print(result, f"{time.perf_counter() - start:.2f}s; the ticks kept running")

asyncio.run(main())
```

## Practice

1. Write a coroutine that "downloads" 10 files concurrently with random delays.
2. Compare the total time of sequential `await`s with `gather`.
3. What goes wrong if you use `time.sleep` inside a coroutine? Try it.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

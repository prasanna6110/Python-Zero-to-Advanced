# Day 111 · Async Iterators, Async Generators and Async Context Managers

_Ultra Advanced_

## The async versions of the protocols
| Sync | Async | Used with |
|------|-------|-----------|
| `__iter__` / `__next__` | `__aiter__` / `__anext__` (raises `StopAsyncIteration`) | `async for` |
| generator (`yield`) | **async generator** (`async def` + `yield`) | `async for` |
| `__enter__` / `__exit__` | `__aenter__` / `__aexit__` | `async with` |
| `@contextmanager` | `@asynccontextmanager` | `async with` |
| comprehension | `[x async for x in agen()]` | inside a coroutine |

## Real-world uses
Streaming API responses, reading database cursors, pages of results, WebSocket messages, and connection pools.

## Examples

### Example 1: An async iterator class and an async generator  ([`example_1.py`](example_1.py))

```python
import asyncio

class Ticker:
    def __init__(self, n, delay):
        self.n, self.delay, self.i = n, delay, 0
    def __aiter__(self):
        return self
    async def __anext__(self):
        if self.i >= self.n:
            raise StopAsyncIteration
        await asyncio.sleep(self.delay)
        self.i += 1
        return self.i

async def fetch_pages(total):
    for page in range(1, total + 1):
        await asyncio.sleep(0.05)          # pretend network call
        yield {"page": page, "items": [f"item{page}-{i}" for i in range(2)]}

async def main():
    async for t in Ticker(3, 0.05):
        print("tick", t)
    async for page in fetch_pages(3):
        print(page)
    squares = [x * x async for x in Ticker(4, 0)]
    print("async comprehension:", squares)

asyncio.run(main())
```

### Example 2: Async context managers  ([`example_2.py`](example_2.py))

```python
import asyncio
from contextlib import asynccontextmanager

class DatabaseConnection:
    async def __aenter__(self):
        await asyncio.sleep(0.05)
        print("connected")
        return self
    async def query(self, sql):
        await asyncio.sleep(0.05)
        return f"result of {sql!r}"
    async def __aexit__(self, exc_type, exc, tb):
        await asyncio.sleep(0.05)
        print("disconnected", "(after error)" if exc_type else "")
        return False

@asynccontextmanager
async def transaction(name):
    print(f"BEGIN {name}")
    try:
        yield
        print(f"COMMIT {name}")
    except Exception:
        print(f"ROLLBACK {name}")
        raise

async def main():
    async with DatabaseConnection() as db:
        print(await db.query("SELECT 1"))
    try:
        async with transaction("payment"):
            raise ValueError("card declined")
    except ValueError:
        pass

asyncio.run(main())
```

### Example 3: An async connection pool  ([`example_3.py`](example_3.py))

```python
import asyncio

class Pool:
    def __init__(self, size):
        self._q = asyncio.Queue()
        for i in range(size):
            self._q.put_nowait(f"conn-{i}")

    def acquire(self):
        pool = self
        class _Ctx:
            async def __aenter__(self):
                self.conn = await pool._q.get()
                return self.conn
            async def __aexit__(self, *exc):
                pool._q.put_nowait(self.conn)
        return _Ctx()

async def handle(pool, req):
    async with pool.acquire() as conn:
        print(f"request {req} using {conn}")
        await asyncio.sleep(0.1)

async def main():
    pool = Pool(2)
    await asyncio.gather(*(handle(pool, r) for r in range(5)))

asyncio.run(main())
```

## Practice

1. Write an async generator that yields lines from a (simulated) live log stream.
2. Write an async rate limiter that works as a context manager.
3. Merge two async generators into one stream.

---

[⬅ Day 110](../Day-110-Build-Your-Own-Event-Loop-How-async-Really-Works/README.md) · [🏠 Home](../README.md) · [Day 112 ➡](../Day-112-contextvars-Context-Local-State/README.md)

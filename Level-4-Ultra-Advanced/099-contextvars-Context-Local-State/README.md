# 099 · contextvars: Context-Local State

## The problem
Global variables, and even `threading.local`, **leak between async tasks**, because every task runs on the same thread. For example, the "current request ID" would get mixed up between requests.

## contextvars (PEP 567)
```python
from contextvars import ContextVar
request_id: ContextVar[str] = ContextVar("request_id", default="-")
token = request_id.set("abc")
request_id.get()
request_id.reset(token)
```
- Every asyncio **Task gets a copy** of the current context when it is created.
- `contextvars.copy_context().run(func)` runs a function inside its own context.
- Web frameworks use this for the current request or user, tracing IDs and database sessions.

## Examples

### Example 1: Why globals break with async  ([`example_1.py`](example_1.py))

```python
import asyncio

current_user = None                    # global: shared by every task!

async def handle(user, delay):
    global current_user
    current_user = user
    await asyncio.sleep(delay)
    print(f"handling {user}, but current_user is {current_user}")

async def main():
    await asyncio.gather(handle("asha", 0.2), handle("ravi", 0.1))

asyncio.run(main())
```

### Example 2: ContextVar fixes it  ([`example_2.py`](example_2.py))

```python
import asyncio
from contextvars import ContextVar

current_user: ContextVar[str] = ContextVar("current_user", default="anonymous")

def log(msg):
    print(f"[user={current_user.get()}] {msg}")

async def handle(user, delay):
    current_user.set(user)
    await asyncio.sleep(delay)
    log("finished request")

async def main():
    await asyncio.gather(handle("asha", 0.2), handle("ravi", 0.1))
    log("back in main")

asyncio.run(main())
```

### Example 3: Request IDs, tokens and copy_context  ([`example_3.py`](example_3.py))

```python
import asyncio, uuid
from contextvars import ContextVar, copy_context

request_id = ContextVar("request_id", default="no-request")

def logger(msg):
    print(f"{request_id.get()[:8]} | {msg}")

async def db_query():
    await asyncio.sleep(0.01)
    logger("db query ran")              # no need to pass the ID along!

async def endpoint(n):
    token = request_id.set(str(uuid.uuid4()))
    try:
        logger(f"start request {n}")
        await db_query()
    finally:
        request_id.reset(token)

async def main():
    await asyncio.gather(*(endpoint(i) for i in range(3)))

asyncio.run(main())
ctx = copy_context()
ctx.run(request_id.set, "isolated-ctx")
print("inside the copied context:", ctx[request_id], "| outside:", request_id.get())
```

## Practice

1. Store a "current locale" in a ContextVar and format messages with it in several tasks.
2. Write a decorator that sets a ContextVar for the duration of a function call.
3. Compare `threading.local` with `ContextVar` inside asyncio.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

# 097 · Build Your Own Event Loop (How async Really Works)

## Under the hood of asyncio
- A coroutine is a generator-like object that **suspends** at `await`.
- `await x` asks `x.__await__()` for an iterator and **yields up** whatever it yields, all the way to the event loop.
- The **event loop** keeps a queue of ready tasks. It calls `task.send(None)`, looks at what was yielded (for example "sleep for 2 seconds" or "wait for this socket") and decides when to resume the task.

## Building blocks
1. **Awaitables**: an object with `__await__` that yields a request to the loop.
2. **Tasks**: wrappers that drive a coroutine and store its result.
3. **Scheduler**: a ready queue plus a heap of sleeping tasks, ordered by wake-up time.
4. **I/O readiness**: the `selectors` module (epoll/kqueue) tells you when sockets are ready.

Once you can build this, asyncio stops being magic.

## Examples

### Example 1: A minimal round-robin scheduler with generators  ([`example_1.py`](example_1.py))

```python
from collections import deque

def task(name, steps):
    for i in range(steps):
        print(f"{name} step {i}")
        yield                     # hand control back to the scheduler

class Scheduler:
    def __init__(self):
        self.ready = deque()
    def spawn(self, gen):
        self.ready.append(gen)
    def run(self):
        while self.ready:
            gen = self.ready.popleft()
            try:
                next(gen)
                self.ready.append(gen)
            except StopIteration:
                pass

s = Scheduler()
s.spawn(task("A", 3))
s.spawn(task("B", 2))
s.spawn(task("C", 1))
s.run()
```

### Example 2: A real async/await event loop with sleep  ([`example_2.py`](example_2.py))

```python
import heapq, time
from collections import deque

class Sleep:
    def __init__(self, seconds): self.seconds = seconds
    def __await__(self):
        yield self                    # hand this request to the loop

class Task:
    def __init__(self, coro): self.coro, self.result, self.done = coro, None, False

class EventLoop:
    def __init__(self):
        self.ready, self.sleeping, self.counter = deque(), [], 0
    def create_task(self, coro):
        t = Task(coro); self.ready.append(t); return t
    def run_until_complete(self, coro):
        main = self.create_task(coro)
        while self.ready or self.sleeping:
            if not self.ready:
                wake, _, t = heapq.heappop(self.sleeping)
                time.sleep(max(0, wake - time.monotonic()))
                self.ready.append(t)
            t = self.ready.popleft()
            try:
                request = t.coro.send(None)
                if isinstance(request, Sleep):
                    self.counter += 1
                    heapq.heappush(self.sleeping, (time.monotonic() + request.seconds, self.counter, t))
            except StopIteration as e:
                t.result, t.done = e.value, True
        return main.result

loop = EventLoop()

async def worker(name, delay):
    print(f"{name}: start")
    await Sleep(delay)
    print(f"{name}: woke after {delay}s")
    return f"{name} done"

async def main():
    tasks = [loop.create_task(worker(n, d)) for n, d in [("fast", 0.2), ("slow", 0.6), ("mid", 0.4)]]
    while not all(t.done for t in tasks):
        await Sleep(0.05)
    return [t.result for t in tasks]

start = time.perf_counter()
print(loop.run_until_complete(main()), f"in {time.perf_counter() - start:.2f}s")
```

### Example 3: A non-blocking socket server using selectors (what asyncio uses)  ([`example_3.py`](example_3.py))

```python
import selectors, socket, threading, time

sel = selectors.DefaultSelector()
server = socket.socket()
server.bind(("127.0.0.1", 0)); server.listen(); server.setblocking(False)
port = server.getsockname()[1]
sel.register(server, selectors.EVENT_READ, data=None)

def run_server(max_msgs):
    handled = 0
    while handled < max_msgs:
        for key, _ in sel.select(timeout=1):
            if key.data is None:                       # a new connection
                conn, _ = key.fileobj.accept()
                conn.setblocking(False)
                sel.register(conn, selectors.EVENT_READ, data="client")
            else:                                      # a client sent data
                data = key.fileobj.recv(1024)
                if data:
                    key.fileobj.sendall(b"pong:" + data); handled += 1
                else:
                    sel.unregister(key.fileobj); key.fileobj.close()

t = threading.Thread(target=run_server, args=(3,), daemon=True); t.start()
clients = [socket.create_connection(("127.0.0.1", port)) for _ in range(3)]
for i, c in enumerate(clients):
    c.sendall(f"client{i}".encode())
for c in clients:
    print(c.recv(1024).decode()); c.close()
t.join(2); server.close()
print("One thread served 3 clients concurrently using selectors.")
```

## Practice

1. Add a `gather()` function to the toy event loop.
2. Add a `Future` type that one task can set and another can await.
3. Change the selectors server so it echoes until the client disconnects.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

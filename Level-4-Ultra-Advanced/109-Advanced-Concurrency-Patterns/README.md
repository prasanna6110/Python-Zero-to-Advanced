# 109 · Advanced Concurrency Patterns

## More synchronisation tools
| Tool | Use |
|------|-----|
| `threading.Condition` | wait until shared state meets a condition (`wait_for(predicate)`) |
| `threading.Barrier(n)` | n threads wait for each other before moving on together |
| `threading.Timer` | run something after a delay |
| `RLock` | a lock the same thread can take more than once |
| `queue.PriorityQueue`, `LifoQueue` | ordered work queues |

## Mixing threads and asyncio
- `loop.run_in_executor(pool, fn)` / `asyncio.to_thread(fn)`: run blocking code **from** async code.
- `asyncio.run_coroutine_threadsafe(coro, loop)`: submit a coroutine **from another thread**.
- `loop.call_soon_threadsafe(cb)`: schedule a callback safely from another thread.

## Patterns
- **Actor model**: each actor has a private mailbox (a queue) and processes one message at a time, so there's no shared state.
- **Worker pool with graceful shutdown**: use a sentinel value or an Event.
- **Map-reduce**, **pipelines** and **fan-out/fan-in**.

## Examples

### Example 1: Condition and Barrier  ([`example_1.py`](example_1.py))

```python
import threading, time

items, cond = [], threading.Condition()

def consumer(name):
    with cond:
        cond.wait_for(lambda: len(items) >= 3)
        print(f"{name} sees batch: {items[:3]}")

def producer():
    for i in range(3):
        time.sleep(0.05)
        with cond:
            items.append(i)
            cond.notify_all()

ts = [threading.Thread(target=consumer, args=(f"C{i}",)) for i in range(2)]
ts.append(threading.Thread(target=producer))
for t in ts: t.start()
for t in ts: t.join()

barrier = threading.Barrier(3, action=lambda: print("--- all runners ready, GO! ---"))
def runner(n):
    time.sleep(0.05 * n)
    print(f"runner {n} at the start line")
    barrier.wait()
    print(f"runner {n} running")
rs = [threading.Thread(target=runner, args=(i,)) for i in range(3)]
for r in rs: r.start()
for r in rs: r.join()
```

### Example 2: The actor model with threads and queues  ([`example_2.py`](example_2.py))

```python
import threading, queue

class Actor(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.mailbox = queue.Queue()
    def send(self, msg):
        self.mailbox.put(msg)
    def run(self):
        while (msg := self.mailbox.get()) is not None:
            self.receive(msg)
    def stop(self):
        self.mailbox.put(None); self.join()

class BankAccount(Actor):
    def __init__(self):
        super().__init__(); self.balance = 0
    def receive(self, msg):
        match msg:
            case ("deposit", amt): self.balance += amt
            case ("withdraw", amt) if amt <= self.balance: self.balance -= amt
            case ("balance", reply_q): reply_q.put(self.balance)

acct = BankAccount(); acct.start()
workers = [threading.Thread(target=lambda: [acct.send(("deposit", 1)) for _ in range(1000)]) for _ in range(5)]
for w in workers: w.start()
for w in workers: w.join()
acct.send(("withdraw", 300))
reply = queue.Queue(); acct.send(("balance", reply))
print("final balance (no locks needed):", reply.get())
acct.stop()
```

### Example 3: Bridging threads and asyncio  ([`example_3.py`](example_3.py))

```python
import asyncio, threading, time

def blocking_report():
    time.sleep(0.3)
    return "report.pdf generated"

async def async_job(n):
    await asyncio.sleep(0.1)
    return f"async job {n} done"

async def main():
    loop = asyncio.get_running_loop()
    report = loop.run_in_executor(None, blocking_report)
    print(await asyncio.gather(report, async_job(1)))

    def background_thread():
        fut = asyncio.run_coroutine_threadsafe(async_job(2), loop)
        print("from thread:", fut.result(timeout=2))
        loop.call_soon_threadsafe(print, "callback scheduled from a thread")
    t = threading.Thread(target=background_thread); t.start()
    while t.is_alive():
        await asyncio.sleep(0.05)
    await asyncio.sleep(0)

asyncio.run(main())
```

## Practice

1. Build a pipeline of 3 stages, each a thread linked by Queues: download → parse → save.
2. Implement a read-write lock (many readers or one writer) with a Condition.
3. Write an asyncio app that receives jobs from a thread-based GUI or keyboard listener.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

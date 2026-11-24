# 097 · Build Your Own Event Loop (How async Really Works) — Example 2: A real async/await event loop with sleep
# Run: python example_2.py

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

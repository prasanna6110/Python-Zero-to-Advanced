# 097 · Build Your Own Event Loop (How async Really Works) — Example 1: A minimal round-robin scheduler with generators
# Run: python example_1.py

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

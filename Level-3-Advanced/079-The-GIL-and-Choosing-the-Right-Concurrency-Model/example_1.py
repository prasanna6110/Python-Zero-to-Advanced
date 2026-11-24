# 079 · The GIL and Choosing the Right Concurrency Model — Example 1: Threads do NOT speed up CPU-bound work
# Run: python example_1.py

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

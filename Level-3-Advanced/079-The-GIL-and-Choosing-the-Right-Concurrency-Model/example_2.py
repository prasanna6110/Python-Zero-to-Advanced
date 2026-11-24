# 079 · The GIL and Choosing the Right Concurrency Model — Example 2: Comparing all three on an I/O task
# Run: python example_2.py

import asyncio, threading, time
from concurrent.futures import ThreadPoolExecutor

N, DELAY = 20, 0.2

def io_task(_):
    time.sleep(DELAY)

async def aio_task():
    await asyncio.sleep(DELAY)

t = time.perf_counter()
for i in range(N): io_task(i)
print(f"sequential : {time.perf_counter() - t:.2f}s")

t = time.perf_counter()
with ThreadPoolExecutor(N) as ex: list(ex.map(io_task, range(N)))
print(f"threads    : {time.perf_counter() - t:.2f}s")

async def main(): await asyncio.gather(*(aio_task() for _ in range(N)))
t = time.perf_counter(); asyncio.run(main())
print(f"asyncio    : {time.perf_counter() - t:.2f}s")

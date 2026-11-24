# 078 · asyncio Advanced: Tasks, Timeouts, Queues and Semaphores — Example 1: Semaphore limiting concurrency
# Run: python example_1.py

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

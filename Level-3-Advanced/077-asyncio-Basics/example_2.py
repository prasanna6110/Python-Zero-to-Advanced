# 077 · asyncio Basics — Example 2: Concurrency with gather and create_task
# Run: python example_2.py

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

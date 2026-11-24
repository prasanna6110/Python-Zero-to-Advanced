# 077 · asyncio Basics — Example 3: Blocking vs non-blocking and to_thread
# Run: python example_3.py

import asyncio, time

def blocking_io():
    time.sleep(1)                 # a legacy blocking call
    return "blocking done"

async def ticker():
    for i in range(3):
        print("  tick", i)
        await asyncio.sleep(0.3)

async def main():
    start = time.perf_counter()
    result, _ = await asyncio.gather(asyncio.to_thread(blocking_io), ticker())
    print(result, f"{time.perf_counter() - start:.2f}s; the ticks kept running")

asyncio.run(main())

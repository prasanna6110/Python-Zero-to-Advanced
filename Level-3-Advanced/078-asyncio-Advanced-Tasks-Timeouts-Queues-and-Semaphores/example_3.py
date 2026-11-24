# 078 · asyncio Advanced: Tasks, Timeouts, Queues and Semaphores — Example 3: Async producer-consumer with workers
# Run: python example_3.py

import asyncio, random

async def producer(q, n):
    for i in range(n):
        await q.put(f"job-{i}")
    print("producer done")

async def worker(name, q, results):
    while True:
        job = await q.get()
        await asyncio.sleep(random.uniform(0.05, 0.2))
        results.append((name, job))
        q.task_done()

async def main():
    random.seed(0)
    q, results = asyncio.Queue(), []
    workers = [asyncio.create_task(worker(f"W{i}", q, results)) for i in range(3)]
    await producer(q, 9)
    await q.join()                 # wait until every job is done
    for w in workers:
        w.cancel()
    await asyncio.gather(*workers, return_exceptions=True)
    for name, job in results:
        print(name, job)

asyncio.run(main())

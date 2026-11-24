# 078 · asyncio Advanced: Tasks, Timeouts, Queues and Semaphores — Example 2: Timeouts, cancellation and TaskGroup
# Run: python example_2.py

import asyncio

async def slow():
    try:
        await asyncio.sleep(10)
    except asyncio.CancelledError:
        print("  slow() was cancelled, cleaning up")
        raise

async def boom():
    await asyncio.sleep(0.1)
    raise ValueError("boom!")

async def main():
    try:
        async with asyncio.timeout(0.3):
            await slow()
    except TimeoutError:
        print("Timed out!")

    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(slow())
            tg.create_task(boom())
    except* ValueError as eg:
        print("TaskGroup failed:", [str(e) for e in eg.exceptions])

    results = await asyncio.gather(boom(), asyncio.sleep(0, "ok"), return_exceptions=True)
    print(results)

asyncio.run(main())

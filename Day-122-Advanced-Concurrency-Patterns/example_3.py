# Day 122 · Advanced Concurrency Patterns — Bridging threads and asyncio
# Run: python example_3.py

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

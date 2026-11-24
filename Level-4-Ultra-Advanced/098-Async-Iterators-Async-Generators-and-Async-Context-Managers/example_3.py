# 098 · Async Iterators, Async Generators and Async Context Managers — Example 3: An async connection pool
# Run: python example_3.py

import asyncio

class Pool:
    def __init__(self, size):
        self._q = asyncio.Queue()
        for i in range(size):
            self._q.put_nowait(f"conn-{i}")

    def acquire(self):
        pool = self
        class _Ctx:
            async def __aenter__(self):
                self.conn = await pool._q.get()
                return self.conn
            async def __aexit__(self, *exc):
                pool._q.put_nowait(self.conn)
        return _Ctx()

async def handle(pool, req):
    async with pool.acquire() as conn:
        print(f"request {req} using {conn}")
        await asyncio.sleep(0.1)

async def main():
    pool = Pool(2)
    await asyncio.gather(*(handle(pool, r) for r in range(5)))

asyncio.run(main())

# Day 111 · Async Iterators, Async Generators and Async Context Managers — An async iterator class and an async generator
# Run: python example_1.py

import asyncio

class Ticker:
    def __init__(self, n, delay):
        self.n, self.delay, self.i = n, delay, 0
    def __aiter__(self):
        return self
    async def __anext__(self):
        if self.i >= self.n:
            raise StopAsyncIteration
        await asyncio.sleep(self.delay)
        self.i += 1
        return self.i

async def fetch_pages(total):
    for page in range(1, total + 1):
        await asyncio.sleep(0.05)          # pretend network call
        yield {"page": page, "items": [f"item{page}-{i}" for i in range(2)]}

async def main():
    async for t in Ticker(3, 0.05):
        print("tick", t)
    async for page in fetch_pages(3):
        print(page)
    squares = [x * x async for x in Ticker(4, 0)]
    print("async comprehension:", squares)

asyncio.run(main())

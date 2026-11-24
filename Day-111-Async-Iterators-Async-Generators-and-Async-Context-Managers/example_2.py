# Day 111 · Async Iterators, Async Generators and Async Context Managers — Async context managers
# Run: python example_2.py

import asyncio
from contextlib import asynccontextmanager

class DatabaseConnection:
    async def __aenter__(self):
        await asyncio.sleep(0.05)
        print("connected")
        return self
    async def query(self, sql):
        await asyncio.sleep(0.05)
        return f"result of {sql!r}"
    async def __aexit__(self, exc_type, exc, tb):
        await asyncio.sleep(0.05)
        print("disconnected", "(after error)" if exc_type else "")
        return False

@asynccontextmanager
async def transaction(name):
    print(f"BEGIN {name}")
    try:
        yield
        print(f"COMMIT {name}")
    except Exception:
        print(f"ROLLBACK {name}")
        raise

async def main():
    async with DatabaseConnection() as db:
        print(await db.query("SELECT 1"))
    try:
        async with transaction("payment"):
            raise ValueError("card declined")
    except ValueError:
        pass

asyncio.run(main())

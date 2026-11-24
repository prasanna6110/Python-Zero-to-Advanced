# Day 112 · contextvars: Context-Local State — ContextVar fixes it
# Run: python example_2.py

import asyncio
from contextvars import ContextVar

current_user: ContextVar[str] = ContextVar("current_user", default="anonymous")

def log(msg):
    print(f"[user={current_user.get()}] {msg}")

async def handle(user, delay):
    current_user.set(user)
    await asyncio.sleep(delay)
    log("finished request")

async def main():
    await asyncio.gather(handle("asha", 0.2), handle("ravi", 0.1))
    log("back in main")

asyncio.run(main())

# Day 112 · contextvars: Context-Local State — Request IDs, tokens and copy_context
# Run: python example_3.py

import asyncio, uuid
from contextvars import ContextVar, copy_context

request_id = ContextVar("request_id", default="no-request")

def logger(msg):
    print(f"{request_id.get()[:8]} | {msg}")

async def db_query():
    await asyncio.sleep(0.01)
    logger("db query ran")              # no need to pass the ID along!

async def endpoint(n):
    token = request_id.set(str(uuid.uuid4()))
    try:
        logger(f"start request {n}")
        await db_query()
    finally:
        request_id.reset(token)

async def main():
    await asyncio.gather(*(endpoint(i) for i in range(3)))

asyncio.run(main())
ctx = copy_context()
ctx.run(request_id.set, "isolated-ctx")
print("inside the copied context:", ctx[request_id], "| outside:", request_id.get())

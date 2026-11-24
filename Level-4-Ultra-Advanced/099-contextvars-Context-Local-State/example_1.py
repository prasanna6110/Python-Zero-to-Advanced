# 099 · contextvars: Context-Local State — Example 1: Why globals break with async
# Run: python example_1.py

import asyncio

current_user = None                    # global: shared by every task!

async def handle(user, delay):
    global current_user
    current_user = user
    await asyncio.sleep(delay)
    print(f"handling {user}, but current_user is {current_user}")

async def main():
    await asyncio.gather(handle("asha", 0.2), handle("ravi", 0.1))

asyncio.run(main())

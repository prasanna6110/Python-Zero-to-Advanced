# 077 · asyncio Basics — Example 1: Your first coroutine
# Run: python example_1.py

import asyncio

async def greet(name, delay):
    print(f"Hello {name} (waiting {delay}s)")
    await asyncio.sleep(delay)
    print(f"Goodbye {name}")
    return name.upper()

async def main():
    result = await greet("Asha", 0.5)
    print("Result:", result)

coro = greet("test", 0)
print(type(coro))
coro.close()                  # creating a coroutine doesn't run it
asyncio.run(main())

# Day 056 · Decorators — Your first decorator
# Run: python example_1.py

import functools

def announce(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f">> calling {func.__name__}{args}")
        result = func(*args, **kwargs)
        print(f"<< {func.__name__} returned {result}")
        return result
    return wrapper

@announce
def add(a, b):
    """Add two numbers."""
    return a + b

add(3, 4)
print(add.__name__, "|", add.__doc__)   # preserved thanks to wraps

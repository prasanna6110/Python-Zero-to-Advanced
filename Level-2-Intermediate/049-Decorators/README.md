# 049 · Decorators

## What is a decorator?
A function that **takes a function and returns a new function** that adds behaviour, without changing the original code.

```python
@my_decorator
def greet(): ...
# is exactly the same as:
greet = my_decorator(greet)
```
## Template
```python
import functools

def my_decorator(func):
    @functools.wraps(func)       # keeps the name and docstring
    def wrapper(*args, **kwargs):
        # before
        result = func(*args, **kwargs)
        # after
        return result
    return wrapper
```
## Common uses
Logging, timing, access control, caching, retrying and validation.

Decorators can be **stacked**. They are applied from the bottom up.

## Examples

### Example 1: Your first decorator  ([`example_1.py`](example_1.py))

```python
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
```

### Example 2: A timing decorator  ([`example_2.py`](example_2.py))

```python
import functools, time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.4f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(i * i for i in range(n))

print(slow_sum(1_000_000))
```

### Example 3: Stacking decorators and access control  ([`example_3.py`](example_3.py))

```python
import functools

current_user = {"name": "prasanna", "role": "admin"}

def require_admin(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if current_user["role"] != "admin":
            raise PermissionError("admins only")
        return func(*args, **kwargs)
    return wrapper

def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"**{func(*args, **kwargs)}**"
    return wrapper

@bold
@require_admin
def delete_user(name):
    return f"deleted {name}"

print(delete_user("spammer"))
current_user["role"] = "guest"
try:
    delete_user("someone")
except PermissionError as e:
    print("Blocked:", e)
```

## Practice

1. Write a `@debug` decorator that prints the arguments and the return value.
2. Write a `@count_calls` decorator that counts how many times a function was called.
3. Stack `@bold` and `@italic` and check which one is applied first.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

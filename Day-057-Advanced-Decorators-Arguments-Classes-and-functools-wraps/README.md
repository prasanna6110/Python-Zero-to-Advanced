# Day 057 · Advanced Decorators: Arguments, Classes and functools.wraps

_Intermediate_

## Decorators that take arguments
These need **three levels** of functions:
```python
def repeat(n):            # 1. receives the decorator's argument
    def decorator(func):  # 2. receives the function
        @wraps(func)
        def wrapper(*a, **kw):  # 3. replaces the function
            ...
        return wrapper
    return decorator

@repeat(3)
def hi(): ...
```
## Class-based decorators
A class with `__call__` can act as a decorator. It's handy when the decorator needs to keep state.

## Decorating classes
A decorator can also receive a **class** and change it or register it (that's how `@dataclass` works).

## Why `functools.wraps`?
Without it, the wrapped function loses its `__name__`, `__doc__` and so on, which breaks debugging and documentation tools.

## Examples

### Example 1: A decorator with arguments: retry  ([`example_1.py`](example_1.py))

```python
import functools

def retry(times=3, exceptions=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"  attempt {attempt} failed: {e}")
            raise RuntimeError(f"{func.__name__} failed after {times} attempts")
        return wrapper
    return decorator

calls = {"n": 0}

@retry(times=4, exceptions=(ConnectionError,))
def flaky_download():
    calls["n"] += 1
    if calls["n"] < 3:
        raise ConnectionError("network down")
    return "file.zip downloaded"

print(flaky_download())
```

### Example 2: A class-based decorator with state  ([`example_2.py`](example_2.py))

```python
import functools

class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)

@CountCalls
def say(msg):
    return msg

say("a"); say("b"); say("c")
print(say.__name__, "was called", say.calls, "times")
```

### Example 3: Class decorators and a registry  ([`example_3.py`](example_3.py))

```python
PLUGINS = {}

def register(name):
    def decorator(cls):
        PLUGINS[name] = cls
        cls.plugin_name = name
        return cls
    return decorator

@register("csv")
class CSVExporter:
    def export(self, rows): return "\n".join(",".join(map(str, r)) for r in rows)

@register("tsv")
class TSVExporter:
    def export(self, rows): return "\n".join("\t".join(map(str, r)) for r in rows)

data = [(1, "a"), (2, "b")]
for name, cls in PLUGINS.items():
    print(f"[{name}]\n{cls().export(data)}")
```

## Practice

1. Write `@rate_limit(calls_per_second)`.
2. Write `@validate_types` that checks arguments against the function's annotations.
3. Write a class decorator that adds a `__repr__` to any class.

---

[⬅ Day 056](../Day-056-Decorators/README.md) · [🏠 Home](../README.md) · [Day 058 ➡](../Day-058-Context-Managers-with-and-contextlib/README.md)

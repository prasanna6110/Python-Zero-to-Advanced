# 096 · Generator Internals: send, throw, close and yield from

## Generators are two-way
`yield` is an **expression**, so it can also **receive** values.
| Method | What it does |
|--------|--------------|
| `next(gen)` / `gen.send(None)` | resumes; `yield` evaluates to None |
| `gen.send(value)` | resumes; `yield` evaluates to `value` |
| `gen.throw(exc)` | raises `exc` **at** the paused `yield` |
| `gen.close()` | raises `GeneratorExit` at the `yield` so the generator can clean up |

You must **prime** a generator (`next(gen)`) before you can send it a value.

## `yield from sub` (PEP 380)
- Hands control to a sub-generator, passing `send` and `throw` straight through.
- Evaluates to the sub-generator's **return value** (`return x` inside a generator ends up in `StopIteration.value`).
- This is exactly the mechanism that `async`/`await` grew out of.

## Generator states
`inspect.getgeneratorstate(gen)` gives `GEN_CREATED`, `GEN_RUNNING`, `GEN_SUSPENDED` or `GEN_CLOSED`.

## Examples

### Example 1: send(): a running-average coroutine  ([`example_1.py`](example_1.py))

```python
import inspect

def averager():
    total = count = 0
    average = None
    while True:
        value = yield average          # receives a value, sends back the average
        total += value
        count += 1
        average = total / count

avg = averager()
print(inspect.getgeneratorstate(avg))
next(avg)                              # prime it
print(inspect.getgeneratorstate(avg))
for v in [10, 20, 30, 100]:
    print(f"sent {v:>3} -> average {avg.send(v):.2f}")
avg.close()
print(inspect.getgeneratorstate(avg))
```

### Example 2: throw() and close() for control and cleanup  ([`example_2.py`](example_2.py))

```python
class ResetSignal(Exception):
    pass

def counter():
    n = 0
    try:
        while True:
            try:
                yield n
                n += 1
            except ResetSignal:
                print("  -> reset received")
                n = 0
    finally:
        print("  -> generator closed, releasing resources")

c = counter()
print(next(c), next(c), next(c))
print("after throw:", c.throw(ResetSignal))
print(next(c))
c.close()
```

### Example 3: yield from: delegation and return values  ([`example_3.py`](example_3.py))

```python
def read_chunk(name):
    total = 0
    while True:
        value = yield
        if value is None:
            return f"{name}: total={total}"    # becomes StopIteration.value
        total += value

def coordinator(results):
    while True:
        name = yield
        summary = yield from read_chunk(name)  # send() passes straight through
        results.append(summary)

results = []
co = coordinator(results)
next(co)
for group, values in {"girls": [40, 42, 39], "boys": [45, 38]}.items():
    co.send(group)
    for v in values:
        co.send(v)
    co.send(None)                              # ends the sub-generator
print(results)

def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item
print(list(flatten([1, [2, [3, [4]], 5]])))
```

## Practice

1. Write a coroutine `grep(pattern)` that receives lines through `send()` and prints the ones that match.
2. Write a generator that you can pause and resume by sending `"pause"` and `"resume"`.
3. Explain why the generator has to be primed before the first `send()`.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

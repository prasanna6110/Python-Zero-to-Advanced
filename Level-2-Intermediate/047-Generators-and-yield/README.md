# 047 · Generators and yield

## Generators
A function that uses `yield` becomes a **generator function**. Calling it returns a generator, which is an iterator.

- `yield` produces a value and **pauses** the function, keeping all its local variables.
- The next call to `next()` **resumes** right after the `yield`.

## Generator expressions
`(x * x for x in range(10))` is like a list comprehension but lazy.

## Why use them?
- **Memory efficient**: you can process a 10 GB file line by line.
- **Infinite sequences** become possible.
- **Pipelines**: you can chain generators like Unix pipes.

`yield from iterable` hands over to another iterable or generator (covered in depth in Level 4).

## Examples

### Example 1: A simple generator  ([`example_1.py`](example_1.py))

```python
def count_up_to(n):
    print("  (generator started)")
    i = 1
    while i <= n:
        yield i
        i += 1
    print("  (generator finished)")

gen = count_up_to(3)
print(type(gen))
print(next(gen))
print(next(gen))
for value in gen:
    print(value)
```

### Example 2: Memory: list vs generator  ([`example_2.py`](example_2.py))

```python
import sys
squares_list = [x * x for x in range(1_000_000)]
squares_gen = (x * x for x in range(1_000_000))
print("list size :", sys.getsizeof(squares_list), "bytes")
print("gen size  :", sys.getsizeof(squares_gen), "bytes")
print("sum from gen:", sum(squares_gen))

def fibonacci():                # an infinite generator
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print([next(fib) for _ in range(12)])
```

### Example 3: A generator pipeline  ([`example_3.py`](example_3.py))

```python
log_lines = [
    "INFO user login",
    "ERROR disk full",
    "INFO page view",
    "ERROR timeout db",
    "WARN slow query",
]

def read(lines):
    for line in lines:
        yield line

def only_errors(lines):
    for line in lines:
        if line.startswith("ERROR"):
            yield line

def messages(lines):
    for line in lines:
        yield line.split(" ", 1)[1].upper()

pipeline = messages(only_errors(read(log_lines)))
for msg in pipeline:
    print(msg)

def chain_all(*iterables):
    for it in iterables:
        yield from it
print(list(chain_all([1, 2], "ab", range(3))))
```

## Practice

1. Write a generator that yields the prime numbers forever.
2. Write a generator that reads a big file in chunks of N lines.
3. Rewrite the custom Countdown iterator from the previous topic as a generator.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

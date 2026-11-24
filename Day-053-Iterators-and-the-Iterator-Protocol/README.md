# Day 053 · Iterators and the Iterator Protocol

_Intermediate_

## Iterable vs iterator
- An **iterable** is anything you can loop over. It has `__iter__()` (lists, strings, dicts, files...).
- An **iterator** is the object that actually produces values one at a time. It has `__iter__()` and `__next__()`, and raises `StopIteration` when it runs out.

`iter(iterable)` gives you an iterator, and `next(iterator)` gives you the next value.

## How a `for` loop really works
```python
it = iter(items)
while True:
    try:
        x = next(it)
    except StopIteration:
        break
    ...
```
## Key facts
- An iterator is **used up** after one pass.
- Iterators are **lazy**: they produce values only when you ask, so they use very little memory.

## Examples

### Example 1: Using iter() and next() by hand  ([`example_1.py`](example_1.py))

```python
nums = [10, 20, 30]
it = iter(nums)
print(next(it), next(it), next(it))
try:
    next(it)
except StopIteration:
    print("Iterator exhausted")
print(next(iter("hi")), type(iter({})))
```

### Example 2: A custom iterator class  ([`example_2.py`](example_2.py))

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for n in Countdown(5):
    print(n, end=" ")
print()
c = Countdown(2)
print(list(c), list(c), "<- exhausted the second time")
```

### Example 3: A reusable iterable (separate iterator object)  ([`example_3.py`](example_3.py))

```python
class Range2:
    """Iterable that can be looped over many times."""
    def __init__(self, start, stop, step=1):
        self.start, self.stop, self.step = start, stop, step

    def __iter__(self):
        current = self.start
        while current < self.stop:
            yield current          # a generator makes a fresh iterator each time
            current += self.step

r = Range2(0, 10, 3)
print(list(r), list(r))
print(sum(r), max(r))
```

## Practice

1. Write an iterator class that returns the Fibonacci numbers up to n.
2. Write an iterator that cycles through a list forever (be careful when testing it!).
3. Why can you loop over a list twice but not over a file object twice?

---

[⬅ Day 052](../Day-052-Enums/README.md) · [🏠 Home](../README.md) · [Day 054 ➡](../Day-054-Generators-and-yield/README.md)

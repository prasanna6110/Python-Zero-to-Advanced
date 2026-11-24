# 051 · Context Managers (with and contextlib)

## Context managers
They set something up and **always clean up afterwards**, even if an error happens.
```python
with open("f.txt") as f:   # f.__enter__() runs here
    ...
# f.__exit__() runs here and the file is closed
```
## Writing your own
**1. As a class:**
- `__enter__(self)` returns the object used in `as`.
- `__exit__(self, exc_type, exc_value, traceback)`: return `True` to **suppress** the exception.

**2. With `@contextlib.contextmanager`:** a generator where the code **before** `yield` is the setup and the code **after** it (in `finally`) is the cleanup.

## Useful tools in contextlib
`suppress`, `redirect_stdout`, `ExitStack` (combine many context managers), `nullcontext` and `closing`.

## Examples

### Example 1: A class-based context manager  ([`example_1.py`](example_1.py))

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"Block took {self.elapsed:.4f}s")
        if exc_type:
            print("An error happened:", exc)
        return False        # don't suppress the error

with Timer() as t:
    total = sum(range(1_000_000))
print("total:", total)
```

### Example 2: @contextmanager  ([`example_2.py`](example_2.py))

```python
from contextlib import contextmanager
import os, tempfile

@contextmanager
def working_directory(path):
    old = os.getcwd()
    os.chdir(path)
    try:
        yield path
    finally:
        os.chdir(old)       # always restored

tmp = tempfile.gettempdir()
print("before:", os.getcwd() != tmp)
with working_directory(tmp) as p:
    print("inside:", os.path.samefile(os.getcwd(), p))
print("after restored:", os.getcwd() != tmp)
```

### Example 3: suppress, redirect_stdout and ExitStack  ([`example_3.py`](example_3.py))

```python
from contextlib import suppress, redirect_stdout, ExitStack
import io, os

with suppress(FileNotFoundError):
    os.remove("no_such_file.txt")
print("No crash thanks to suppress")

buffer = io.StringIO()
with redirect_stdout(buffer):
    print("this goes into the buffer")
print("Captured:", buffer.getvalue().strip())

names = ["f1.txt", "f2.txt", "f3.txt"]
with ExitStack() as stack:
    files = [stack.enter_context(open(n, "w")) for n in names]
    for i, f in enumerate(files):
        f.write(f"file {i}")
print("all closed:", all(f.closed for f in files))
for n in names:
    os.remove(n)
```

## Practice

1. Write a context manager that prints "start" and "end" around a block of code.
2. Write `temporary_file()` that creates a file and deletes it when the block ends.
3. Write a database-transaction-style context manager that rolls back if there's an error.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

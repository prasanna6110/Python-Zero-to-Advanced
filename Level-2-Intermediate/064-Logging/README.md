# 064 · Logging

## Why not just print?
Logging gives you **levels**, timestamps, output to files and fine-grained control, and you can turn it on or off without editing code.

## Levels (lowest to highest)
`DEBUG` < `INFO` < `WARNING` (the default) < `ERROR` < `CRITICAL`

## Basic setup
```python
import logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger(__name__)
log.info("Started")
```
## The pieces
- **Logger**: what your code calls.
- **Handler**: where the logs go (console, file, rotating file).
- **Formatter**: what each line looks like.

`log.exception("msg")` inside an `except` block logs the full traceback.

## Examples

### Example 1: Basic logging  ([`example_1.py`](example_1.py))

```python
import logging, sys

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout,
                    format="%(levelname)-8s %(message)s")
logging.debug("Detailed info for debugging")
logging.info("Server started on port 8000")
logging.warning("Disk usage at 85%")
logging.error("Could not connect to database")
logging.critical("System is shutting down!")
```

### Example 2: Named loggers, handlers and files  ([`example_2.py`](example_2.py))

```python
import logging, sys, os

logger = logging.getLogger("payment")
logger.setLevel(logging.DEBUG)
console = logging.StreamHandler(sys.stdout)
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter("[%(name)s] %(levelname)s: %(message)s"))
file_handler = logging.FileHandler("app.log")
file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
logger.addHandler(console)
logger.addHandler(file_handler)

logger.debug("only in the file")
logger.info("payment received")
file_handler.close()
print("--- app.log contents ---")
print(open("app.log").read().strip())
os.remove("app.log")
```

### Example 3: Logging exceptions  ([`example_3.py`](example_3.py))

```python
import logging, sys

logging.basicConfig(level=logging.INFO, stream=sys.stdout, format="%(levelname)s %(message)s")
log = logging.getLogger("calc")

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        log.exception("Division failed for a=%s b=%s", a, b)
        return None

print(divide(10, 2))
print(divide(1, 0))
```

## Practice

1. Add logging to an earlier project in place of the `print` calls.
2. Set up a `RotatingFileHandler` with a maximum size of 1 MB.
3. Log every function call using a decorator together with the logging module.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

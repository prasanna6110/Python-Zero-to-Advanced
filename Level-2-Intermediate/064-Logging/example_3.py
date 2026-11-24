# 064 · Logging — Example 3: Logging exceptions
# Run: python example_3.py

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

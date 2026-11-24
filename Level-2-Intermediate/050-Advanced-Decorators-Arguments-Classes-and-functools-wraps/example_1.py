# 050 · Advanced Decorators: Arguments, Classes and functools.wraps — Example 1: A decorator with arguments: retry
# Run: python example_1.py

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

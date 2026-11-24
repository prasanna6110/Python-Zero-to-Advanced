# Day 086 · concurrent.futures — submit, as_completed and exceptions
# Run: python example_2.py

from concurrent.futures import ThreadPoolExecutor, as_completed
import time, random

random.seed(3)
def task(n):
    time.sleep(random.uniform(0.1, 0.5))
    if n == 3:
        raise ValueError("task 3 failed")
    return n * n

with ThreadPoolExecutor(4) as ex:
    futures = {ex.submit(task, n): n for n in range(6)}
    for fut in as_completed(futures):
        n = futures[fut]
        try:
            print(f"task {n} finished -> {fut.result()}")
        except ValueError as e:
            print(f"task {n} raised: {e}")

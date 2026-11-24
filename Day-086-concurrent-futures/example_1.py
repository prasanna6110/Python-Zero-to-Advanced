# Day 086 · concurrent.futures — ThreadPoolExecutor.map
# Run: python example_1.py

from concurrent.futures import ThreadPoolExecutor
import time

def fetch(url):
    time.sleep(0.5)
    return f"{url} -> 200 OK"

urls = [f"https://site{i}.com" for i in range(6)]
start = time.perf_counter()
with ThreadPoolExecutor(max_workers=6) as ex:
    for result in ex.map(fetch, urls):
        print(result)
print(f"took {time.perf_counter() - start:.2f}s (not 3s)")

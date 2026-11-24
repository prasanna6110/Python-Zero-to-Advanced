# 104 · The Buffer Protocol and memoryview — Example 1: Zero-copy slicing vs copying
# Run: python example_1.py

import time

data = bytearray(50_000_000)          # 50 MB

start = time.perf_counter()
for _ in range(20):
    chunk = data[10:40_000_000]       # copies 40 MB every time
copy_time = time.perf_counter() - start

mv = memoryview(data)
start = time.perf_counter()
for _ in range(20):
    chunk = mv[10:40_000_000]         # no copy
view_time = time.perf_counter() - start
print(f"bytearray slice: {copy_time:.3f}s | memoryview slice: {view_time:.6f}s")

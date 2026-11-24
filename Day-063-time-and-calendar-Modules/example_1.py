# Day 063 · time and calendar Modules — The time module
# Run: python example_1.py

import time

print("epoch seconds:", round(time.time()))
print("now:", time.ctime())
print(time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()))
start = time.perf_counter()
time.sleep(0.3)
print(f"slept {time.perf_counter() - start:.3f}s")
t = time.localtime()
print("year:", t.tm_year, "day of year:", t.tm_yday)

# Day 084 · Threading — I/O-bound speed-up with threads
# Run: python example_1.py

import threading, time

def download(name, seconds):
    time.sleep(seconds)            # simulates waiting on the network
    print(f"  downloaded {name}")

files = [("a.zip", 1), ("b.zip", 1), ("c.zip", 1)]

start = time.perf_counter()
for f in files:
    download(*f)
print(f"Sequential: {time.perf_counter() - start:.2f}s")

start = time.perf_counter()
threads = [threading.Thread(target=download, args=f) for f in files]
for t in threads: t.start()
for t in threads: t.join()
print(f"Threaded:   {time.perf_counter() - start:.2f}s")

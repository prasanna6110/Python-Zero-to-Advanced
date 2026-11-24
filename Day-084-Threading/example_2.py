# Day 084 · Threading — Race condition and Lock
# Run: python example_2.py

import threading

counter = 0
lock = threading.Lock()

def unsafe(n):
    global counter
    for _ in range(n):
        tmp = counter          # read
        tmp += 1               # modify
        counter = tmp          # write (another thread may have run in between!)

def safe(n):
    global counter
    for _ in range(n):
        with lock:
            counter += 1

for worker in (unsafe, safe):
    counter = 0
    ts = [threading.Thread(target=worker, args=(200_000,)) for _ in range(4)]
    for t in ts: t.start()
    for t in ts: t.join()
    print(f"{worker.__name__}: {counter} (expected 800000)")

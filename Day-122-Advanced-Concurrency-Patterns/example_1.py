# Day 122 · Advanced Concurrency Patterns — Condition and Barrier
# Run: python example_1.py

import threading, time

items, cond = [], threading.Condition()

def consumer(name):
    with cond:
        cond.wait_for(lambda: len(items) >= 3)
        print(f"{name} sees batch: {items[:3]}")

def producer():
    for i in range(3):
        time.sleep(0.05)
        with cond:
            items.append(i)
            cond.notify_all()

ts = [threading.Thread(target=consumer, args=(f"C{i}",)) for i in range(2)]
ts.append(threading.Thread(target=producer))
for t in ts: t.start()
for t in ts: t.join()

barrier = threading.Barrier(3, action=lambda: print("--- all runners ready, GO! ---"))
def runner(n):
    time.sleep(0.05 * n)
    print(f"runner {n} at the start line")
    barrier.wait()
    print(f"runner {n} running")
rs = [threading.Thread(target=runner, args=(i,)) for i in range(3)]
for r in rs: r.start()
for r in rs: r.join()

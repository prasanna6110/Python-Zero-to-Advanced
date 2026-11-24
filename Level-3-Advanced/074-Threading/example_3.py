# 074 · Threading — Example 3: Producer-consumer with queue.Queue
# Run: python example_3.py

import threading, queue, time, random

q = queue.Queue(maxsize=5)
random.seed(1)

def producer():
    for i in range(6):
        item = f"order-{i}"
        q.put(item)
        print(f"produced {item}")
        time.sleep(random.uniform(0.01, 0.05))
    q.put(None)                     # sentinel: tells the consumer to stop

def consumer():
    while (item := q.get()) is not None:
        print(f"        consumed {item}")
        time.sleep(random.uniform(0.02, 0.06))
        q.task_done()

p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)
p.start(); c.start(); p.join(); c.join()
print("All orders processed")

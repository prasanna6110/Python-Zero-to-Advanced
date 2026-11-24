# Day 085 · Multiprocessing — Process, Queue and the separate memory
# Run: python example_2.py

from multiprocessing import Process, Queue
import os

data = []

def worker(q, n):
    data.append(n)                           # only changes the CHILD's copy
    q.put((os.getpid(), n * n))

if __name__ == "__main__":
    q = Queue()
    procs = [Process(target=worker, args=(q, i)) for i in range(4)]
    for p in procs: p.start()
    results = [q.get() for _ in procs]
    for p in procs: p.join()
    print("results:", sorted(r[1] for r in results))
    print("distinct PIDs:", len({r[0] for r in results}), "| main pid:", os.getpid())
    print("parent's data list is still:", data)

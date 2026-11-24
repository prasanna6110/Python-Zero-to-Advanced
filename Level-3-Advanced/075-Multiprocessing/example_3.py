# 075 · Multiprocessing — Example 3: Shared Value, Array and Manager
# Run: python example_3.py

from multiprocessing import Process, Value, Array, Manager, Lock

def add(counter, arr, shared, lock, i):
    with lock:
        counter.value += 1
    arr[i] = i * 10
    shared[f"worker{i}"] = "done"

if __name__ == "__main__":
    counter = Value("i", 0)
    arr = Array("i", 4)
    lock = Lock()
    with Manager() as m:
        shared = m.dict()
        ps = [Process(target=add, args=(counter, arr, shared, lock, i)) for i in range(4)]
        for p in ps: p.start()
        for p in ps: p.join()
        print(counter.value, list(arr), dict(sorted(shared.items())))

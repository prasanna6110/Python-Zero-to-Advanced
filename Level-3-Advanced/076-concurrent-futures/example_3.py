# 076 · concurrent.futures — Example 3: ProcessPoolExecutor for CPU work
# Run: python example_3.py

from concurrent.futures import ProcessPoolExecutor
import math, time

def heavy(n):
    return sum(math.sqrt(i) for i in range(n))

if __name__ == "__main__":
    nums = [3_000_000] * 4
    start = time.perf_counter()
    with ProcessPoolExecutor() as ex:
        results = list(ex.map(heavy, nums))
    print([round(r) for r in results])
    print(f"process pool: {time.perf_counter() - start:.2f}s")

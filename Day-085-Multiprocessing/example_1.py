# Day 085 · Multiprocessing — CPU-bound: sequential vs process pool
# Run: python example_1.py

import time
from multiprocessing import Pool, cpu_count

def count_primes(limit):
    count = 0
    for n in range(2, limit):
        if all(n % d for d in range(2, int(n ** 0.5) + 1)):
            count += 1
    return count

if __name__ == "__main__":
    jobs = [60_000] * 4
    start = time.perf_counter()
    seq = [count_primes(j) for j in jobs]
    t_seq = time.perf_counter() - start

    start = time.perf_counter()
    with Pool(min(4, cpu_count())) as pool:
        par = pool.map(count_primes, jobs)
    t_par = time.perf_counter() - start
    print(f"sequential {t_seq:.2f}s | pool {t_par:.2f}s | same result: {seq == par}")
    print("CPU cores:", cpu_count())

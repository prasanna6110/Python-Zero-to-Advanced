# Day 093 · Performance: Profiling and Optimisation — tracemalloc for memory
# Run: python example_3.py

import tracemalloc

tracemalloc.start()
big_list = [str(i) * 10 for i in range(100_000)]
gen_total = sum(len(str(i) * 10) for i in range(100_000))
snapshot = tracemalloc.take_snapshot()
current, peak = tracemalloc.get_traced_memory()
print(f"current={current / 1e6:.1f} MB peak={peak / 1e6:.1f} MB")
for stat in snapshot.statistics("lineno")[:3]:
    print(stat)
tracemalloc.stop()

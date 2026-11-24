# 022 · Sets — Example 3: Fast membership and frozenset
# Run: python example_3.py

import time
big_list = list(range(1_000_000))
big_set = set(big_list)

t = time.perf_counter(); 999_999 in big_list; list_time = time.perf_counter() - t
t = time.perf_counter(); 999_999 in big_set; set_time = time.perf_counter() - t
print(f"list lookup: {list_time:.6f}s, set lookup: {set_time:.6f}s")

fs = frozenset({"read", "write"})
permissions = {fs: "editor"}       # a frozenset can be a dict key
print(permissions)

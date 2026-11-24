# 056 · math, random and statistics — Example 3: Simulation with statistics: dice rolls
# Run: python example_3.py

import random, statistics
from collections import Counter

random.seed(7)
rolls = [random.randint(1, 6) + random.randint(1, 6) for _ in range(10_000)]
counts = Counter(rolls)
for total in range(2, 13):
    bar = "#" * (counts[total] // 50)
    print(f"{total:>2}: {bar}")
print("mean:", round(statistics.mean(rolls), 3), "mode:", statistics.mode(rolls),
      "stdev:", round(statistics.stdev(rolls), 3))

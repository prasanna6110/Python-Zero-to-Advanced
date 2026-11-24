# 092 · heapq, bisect and array — Example 2: Top-k and merging sorted streams
# Run: python example_2.py

import heapq

words = "the quick brown fox jumps over the lazy dog the fox".split()
from collections import Counter
print(heapq.nlargest(2, Counter(words).items(), key=lambda kv: kv[1]))

log_a = [1, 5, 9]
log_b = [2, 3, 10]
log_c = [4, 8]
print("merged:", list(heapq.merge(log_a, log_b, log_c)))

def running_median(stream):
    low, high = [], []                    # max-heap (negated), min-heap
    for x in stream:
        heapq.heappush(low, -x)
        heapq.heappush(high, -heapq.heappop(low))
        if len(high) > len(low):
            heapq.heappush(low, -heapq.heappop(high))
        yield -low[0] if len(low) > len(high) else (-low[0] + high[0]) / 2
print("running median:", list(running_median([5, 15, 1, 3, 8])))

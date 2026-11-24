# 092 · heapq, bisect and array

## heapq: a min-heap (priority queue) on top of a list
| Function | Cost |
|----------|------|
| `heappush(h, x)` / `heappop(h)` | O(log n) |
| `heapify(list)` | O(n) |
| `nlargest(k, it)` / `nsmallest(k, it)` | efficient top-k |
| `heappushpop`, `heapreplace`, `merge` | combined operations |

For a max-heap, push negated values. For priorities, push tuples: `(priority, counter, item)`.

## bisect: binary search on a **sorted** list
`bisect_left`, `bisect_right` and `insort` work in O(log n) (inserting still shifts items, so it's O(n)). Since 3.10 they also accept `key=`.

## array: compact, typed arrays
`array("i", [1, 2, 3])` stores raw C values and uses much less memory than a list of int objects.

## Examples

### Example 1: Priority queue with heapq  ([`example_1.py`](example_1.py))

```python
import heapq
from itertools import count

tasks = []
c = count()
for priority, task in [(3, "write docs"), (1, "fix prod bug"), (2, "code review"), (1, "reply to client")]:
    heapq.heappush(tasks, (priority, next(c), task))

while tasks:
    p, _, task = heapq.heappop(tasks)
    print(f"[P{p}] {task}")

scores = [88, 42, 99, 73, 65, 91]
print("top 3:", heapq.nlargest(3, scores), "bottom 2:", heapq.nsmallest(2, scores))
```

### Example 2: Top-k and merging sorted streams  ([`example_2.py`](example_2.py))

```python
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
```

### Example 3: bisect and array  ([`example_3.py`](example_3.py))

```python
import bisect, sys
from array import array

def grade(score, cutoffs=[40, 60, 75, 90], grades="FCBAS"):
    return grades[bisect.bisect_right(cutoffs, score)]
print([grade(s) for s in [33, 40, 59, 75, 95]])

sorted_list = [10, 20, 30, 40]
bisect.insort(sorted_list, 25)
print(sorted_list, "insert 35 at index", bisect.bisect_left(sorted_list, 35))

nums_list = list(range(100_000))
nums_array = array("i", range(100_000))
print("list:", sys.getsizeof(nums_list) + sum(sys.getsizeof(n) for n in nums_list[:1]) * len(nums_list), "bytes (approx)")
print("array:", sys.getsizeof(nums_array), "bytes")
```

## Practice

1. Build a hospital emergency queue using heapq.
2. Find the k closest points to the origin.
3. Use bisect to find how many scores fall between 60 and 80 in a sorted list.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

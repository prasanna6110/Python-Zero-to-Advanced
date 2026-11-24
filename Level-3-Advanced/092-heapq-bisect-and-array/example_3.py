# 092 · heapq, bisect and array — Example 3: bisect and array
# Run: python example_3.py

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

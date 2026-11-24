# Day 107 · Algorithms: Searching and Sorting — Merge sort and quick sort
# Run: python example_2.py

import random

def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left, right = merge_sort(a[:mid]), merge_sort(a[mid:])
    out, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    return out + left[i:] + right[j:]

def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = random.choice(a)
    return (quick_sort([x for x in a if x < pivot]) + [x for x in a if x == pivot]
            + quick_sort([x for x in a if x > pivot]))

random.seed(0)
nums = [random.randint(1, 99) for _ in range(12)]
print(nums)
print(merge_sort(nums))
print(quick_sort(nums) == sorted(nums))

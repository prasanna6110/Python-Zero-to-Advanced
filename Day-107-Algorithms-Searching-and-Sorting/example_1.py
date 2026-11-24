# Day 107 · Algorithms: Searching and Sorting — Linear vs binary search
# Run: python example_1.py

def linear_search(arr, target):
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1

def binary_search(arr, target):
    lo, hi, steps = 0, len(arr) - 1, 0
    while lo <= hi:
        steps += 1
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid, steps
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1, steps

data = list(range(0, 1_000_000, 3))
print("linear:", linear_search(data, 999_999))
print("binary (index, steps):", binary_search(data, 999_999))

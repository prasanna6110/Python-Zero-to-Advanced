# 094 · Algorithms: Searching and Sorting

## Searching
| Algorithm | Time | Needs |
|-----------|------|-------|
| Linear search | O(n) | nothing |
| Binary search | O(log n) | sorted data |

## Sorting
| Algorithm | Best | Average | Worst | Stable? |
|-----------|------|---------|-------|---------|
| Bubble | O(n) | O(n²) | O(n²) | yes |
| Insertion | O(n) | O(n²) | O(n²) | yes |
| Merge | O(n log n) | O(n log n) | O(n log n) | yes |
| Quick | O(n log n) | O(n log n) | O(n²) | no |
| Python's `sorted` (Timsort) | O(n) | O(n log n) | O(n log n) | yes |

## Techniques to know
Two pointers, sliding window, divide and conquer, and prefix sums.

## Examples

### Example 1: Linear vs binary search  ([`example_1.py`](example_1.py))

```python
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
```

### Example 2: Merge sort and quick sort  ([`example_2.py`](example_2.py))

```python
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
```

### Example 3: Two pointers, sliding window and prefix sums  ([`example_3.py`](example_3.py))

```python
def pair_with_sum(sorted_nums, target):
    i, j = 0, len(sorted_nums) - 1
    while i < j:
        s = sorted_nums[i] + sorted_nums[j]
        if s == target: return sorted_nums[i], sorted_nums[j]
        i, j = (i + 1, j) if s < target else (i, j - 1)

def max_window_sum(nums, k):
    window = best = sum(nums[:k])
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best

def longest_unique_substring(s):
    seen, start, best = {}, 0, ""
    for i, ch in enumerate(s):
        if seen.get(ch, -1) >= start:
            start = seen[ch] + 1
        seen[ch] = i
        best = max(best, s[start:i + 1], key=len)
    return best

from itertools import accumulate
prefix = [0, *accumulate([3, 1, 4, 1, 5, 9])]
print(pair_with_sum([1, 3, 5, 7, 11], 12))
print(max_window_sum([2, 1, 5, 1, 3, 2], 3))
print(longest_unique_substring("abcabcbb"))
print("sum of index 2..4:", prefix[5] - prefix[2])
```

## Practice

1. Implement insertion sort and count its swaps.
2. Use binary search to find the first and last position of a value in a sorted list.
3. Find the smallest subarray whose sum is at least k (sliding window).

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

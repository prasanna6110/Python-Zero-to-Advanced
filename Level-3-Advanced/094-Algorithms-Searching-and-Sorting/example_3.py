# 094 · Algorithms: Searching and Sorting — Example 3: Two pointers, sliding window and prefix sums
# Run: python example_3.py

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

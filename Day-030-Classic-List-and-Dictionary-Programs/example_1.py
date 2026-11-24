# Day 030 · Classic List and Dictionary Programs — Largest, second largest, missing number and duplicates
# Run: python example_1.py

nums = [12, 45, 7, 45, 23, 89, 7, 56]

largest = second = float("-inf")
for n in nums:
    if n > largest:
        largest, second = n, largest
    elif largest > n > second:
        second = n
print("largest:", largest, "second largest:", second)

seen, dups = set(), set()
for n in nums:
    (dups if n in seen else seen).add(n)
print("duplicates:", dups)

arr = [1, 2, 4, 5, 6]
n = len(arr) + 1
print("missing number:", n * (n + 1) // 2 - sum(arr))
evens = [x for x in nums if x % 2 == 0]
print("evens:", evens, "odds count:", len(nums) - len(evens))
print("rotated left by 2:", nums[2:] + nums[:2])

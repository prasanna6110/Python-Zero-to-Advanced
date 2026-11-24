# Day 127 · Common Mistakes and Gotchas — List and reference gotchas
# Run: python example_1.py

grid = [[0] * 3] * 3
grid[0][0] = 1
print("Bug :", grid)
grid = [[0] * 3 for _ in range(3)]
grid[0][0] = 1
print("Fixed:", grid)

nums = [1, 2, 2, 3, 4]
for n in nums:
    if n == 2:
        nums.remove(n)                 # changing the list while looping over it
print("Bug  (should be [1, 3, 4]):", nums)
nums = [1, 2, 2, 3, 4]
print("Fixed:", [n for n in nums if n != 2])

a = b = []
a.append(1)
print("a = b = [] shares one list:", b)
lst = [3, 1, 2]
print("lst.sort() returns:", lst.sort(), "| sorted(lst) returns:", sorted([3, 1, 2]))

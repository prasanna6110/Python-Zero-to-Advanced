# 020 · List Methods — Example 1: Adding and removing
# Run: python example_1.py

nums = [3, 1, 4]
nums.append(1)
nums.extend([5, 9])
nums.insert(0, 100)
print(nums)
nums.remove(1)       # removes the first 1 only
last = nums.pop()
first = nums.pop(0)
print(nums, "popped:", last, first)

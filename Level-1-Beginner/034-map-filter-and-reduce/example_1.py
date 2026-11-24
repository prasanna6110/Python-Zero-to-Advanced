# 034 · map, filter and reduce — Example 1: map
# Run: python example_1.py

nums = [1, 2, 3, 4]
print(list(map(lambda x: x * x, nums)))
print(list(map(str.upper, ["a", "b"])))
print(list(map(int, "1 2 3".split())))
print(list(map(lambda a, b: a + b, [1, 2, 3], [10, 20, 30])))

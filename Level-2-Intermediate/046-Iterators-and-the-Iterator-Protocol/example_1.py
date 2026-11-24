# 046 · Iterators and the Iterator Protocol — Example 1: Using iter() and next() by hand
# Run: python example_1.py

nums = [10, 20, 30]
it = iter(nums)
print(next(it), next(it), next(it))
try:
    next(it)
except StopIteration:
    print("Iterator exhausted")
print(next(iter("hi")), type(iter({})))

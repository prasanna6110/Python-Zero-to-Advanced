# 034 · map, filter and reduce — Example 2: filter
# Run: python example_2.py

nums = range(1, 21)
print(list(filter(lambda n: n % 3 == 0, nums)))
words = ["", "python", None, "code", 0]
print(list(filter(None, words)))          # removes falsy values
emails = ["a@x.com", "bad", "c@y.org"]
print(list(filter(lambda e: "@" in e, emails)))

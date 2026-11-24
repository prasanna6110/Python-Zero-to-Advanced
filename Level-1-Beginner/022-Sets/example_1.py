# 022 · Sets — Example 1: Removing duplicates
# Run: python example_1.py

emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com", "b@x.com"]
unique = set(emails)
print(unique, len(unique))
s = {1, 2}
s.add(3)
s.update([4, 5])
s.discard(10)       # no error
print(s)

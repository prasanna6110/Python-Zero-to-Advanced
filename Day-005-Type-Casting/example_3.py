# Day 005 · Type Casting — Converting between collections
# Run: python example_3.py

word = "banana"
print(list(word))
print(set(word))            # duplicates are removed
print(tuple([1, 2, 3]))
print(int("1010", 2))       # binary string -> int
print(hex(255), oct(8), bin(5))
print(float("3.14") * 2)

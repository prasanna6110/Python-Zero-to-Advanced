# 025 · Mutable vs Immutable and Copying — Example 3: Shallow vs deep copy
# Run: python example_3.py

import copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0].append(99)
print("original:", original)
print("shallow :", shallow, "<- inner list is shared")
print("deep    :", deep, "<- fully independent")

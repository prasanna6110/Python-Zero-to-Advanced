# Day 071 · itertools — groupby, accumulate, chain, pairwise, batched
# Run: python example_3.py

from itertools import groupby, accumulate, chain, pairwise, batched
import operator

sales = [("Jan", 100), ("Feb", 150), ("Mar", 120)]
print(list(accumulate(s for _, s in sales)))
print(list(accumulate([1, 2, 3, 4], operator.mul)))
data = sorted(["apple", "avocado", "banana", "blueberry", "cherry"], key=lambda w: w[0])
for letter, group in groupby(data, key=lambda w: w[0]):
    print(letter, list(group))
print(list(chain([1, 2], (3, 4), "56")))
print([b - a for a, b in pairwise([10, 13, 19, 30])])
print(list(batched(range(10), 3)))

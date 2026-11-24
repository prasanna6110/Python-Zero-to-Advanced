# Day 030 · Classic List and Dictionary Programs — Merging, two-sum and dictionary tricks
# Run: python example_3.py

def merge_sorted(a, b):
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i]); i += 1
        else:
            out.append(b[j]); j += 1
    return out + a[i:] + b[j:]

def two_sum(nums, target):
    index = {}
    for i, n in enumerate(nums):
        if target - n in index:
            return index[target - n], i
        index[n] = i

marks = {"Asha": 88, "Ravi": 95, "Meera": 72, "Kiran": 95}
print(merge_sorted([1, 4, 9], [2, 3, 10, 12]))
print("two_sum:", two_sum([2, 7, 11, 15], 18))
print("sorted by value:", dict(sorted(marks.items(), key=lambda kv: kv[1], reverse=True)))
inverted = {}
for name, m in marks.items():
    inverted.setdefault(m, []).append(name)
print("inverted:", inverted)
print("toppers:", [k for k, v in marks.items() if v == max(marks.values())])

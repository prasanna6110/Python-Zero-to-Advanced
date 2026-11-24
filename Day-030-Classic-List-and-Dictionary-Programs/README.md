# Day 030 · Classic List and Dictionary Programs

_Beginner_

## Programs to master
- Largest, smallest, second largest (without `sort`)
- Sum, average, count of evens and odds
- Reverse and rotate a list
- Remove duplicates, find the duplicates
- Merge two sorted lists
- Find the missing number in 1..n
- Matrix addition, multiplication and transpose
- Frequency of elements, grouping
- Sort a dict by value, invert a dict
- Two-sum: indices of the two numbers that add up to a target

These questions test whether you **understand loops and collections**, not whether you can memorise built-ins.

## Examples

### Example 1: Largest, second largest, missing number and duplicates  ([`example_1.py`](example_1.py))

```python
nums = [12, 45, 7, 45, 23, 89, 7, 56]

largest = second = float("-inf")
for n in nums:
    if n > largest:
        largest, second = n, largest
    elif largest > n > second:
        second = n
print("largest:", largest, "second largest:", second)

seen, dups = set(), set()
for n in nums:
    (dups if n in seen else seen).add(n)
print("duplicates:", dups)

arr = [1, 2, 4, 5, 6]
n = len(arr) + 1
print("missing number:", n * (n + 1) // 2 - sum(arr))
evens = [x for x in nums if x % 2 == 0]
print("evens:", evens, "odds count:", len(nums) - len(evens))
print("rotated left by 2:", nums[2:] + nums[:2])
```

### Example 2: Matrix operations without libraries  ([`example_2.py`](example_2.py))

```python
A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]

def transpose(M):
    return [list(row) for row in zip(*M)]

def multiply(X, Y):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*Y)] for row in X]

def add(X, Y):
    return [[a + b for a, b in zip(r1, r2)] for r1, r2 in zip(X, Y)]

def show(M, name):
    print(name)
    for row in M:
        print("  ", " ".join(f"{v:4}" for v in row))

show(transpose(A), "Transpose of A:")
show(multiply(A, B), "A x B:")
show(add(A, A), "A + A:")
```

### Example 3: Merging, two-sum and dictionary tricks  ([`example_3.py`](example_3.py))

```python
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
```

## Practice

1. Find the intersection of two lists without using sets.
2. Move all the zeros in a list to the end, keeping the order of the other items.
3. Find the element that appears the most, plus its count.
4. Group a list of words into a dict keyed by word length.

---

[⬅ Day 029](../Day-029-Comprehensions-list-dict-and-set/README.md) · [🏠 Home](../README.md) · [Day 031 ➡](../Day-031-Mutable-vs-Immutable-and-Copying/README.md)

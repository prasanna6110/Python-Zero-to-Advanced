# Day 024 · Lists

_Beginner_

## Lists
An **ordered, mutable** collection that allows duplicates and mixed types: `[1, "a", 3.5]`.

- Indexing and slicing work just like they do for strings.
- Lists are mutable: `lst[0] = 99` works.
- You can nest them: `matrix = [[1, 2], [3, 4]]`.
- `len()`, `min()`, `max()`, `sum()`, `in` and `sorted()` all work on lists.

## Assignment does not copy
`b = a` means both names point to **the same list**. Use `a.copy()`, `a[:]` or `list(a)` to make a copy.

## Examples

### Example 1: Creating and accessing  ([`example_1.py`](example_1.py))

```python
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0], fruits[-1])
print(fruits[1:3])
fruits[1] = "blueberry"
print(fruits)
print("cherry" in fruits, len(fruits))
```

### Example 2: Nested lists (matrix)  ([`example_2.py`](example_2.py))

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print("Middle:", matrix[1][1])
for row in matrix:
    print(" ".join(str(x) for x in row))
diagonal = [matrix[i][i] for i in range(3)]
print("Diagonal:", diagonal)
```

### Example 3: Reference vs copy  ([`example_3.py`](example_3.py))

```python
a = [1, 2, 3]
b = a           # same object
c = a.copy()    # new object
b.append(4)
print("a:", a)
print("b:", b)
print("c:", c)
print(a is b, a is c)
```

## Practice

1. Find the second-largest number in a list without using `sort`.
2. Add two 2x2 matrices stored as nested lists.
3. Rotate a list by k positions using slicing.

---

[⬅ Day 023](../Day-023-Classic-String-Programs/README.md) · [🏠 Home](../README.md) · [Day 025 ➡](../Day-025-List-Methods/README.md)

# 020 · List Methods

| Method | What it does |
|--------|--------------|
| `append(x)` | add one item at the end |
| `extend(iter)` | add many items |
| `insert(i, x)` | insert at index i |
| `remove(x)` | remove the first matching value |
| `pop(i=-1)` | remove and return the item at index i |
| `clear()` | empty the list |
| `index(x)` | position of x |
| `count(x)` | how many times x appears |
| `sort(key=, reverse=)` | sort **in place** (returns None) |
| `reverse()` | reverse in place |
| `copy()` | shallow copy |

`sorted(lst)` returns a **new** list, while `lst.sort()` changes the original.

## Examples

### Example 1: Adding and removing  ([`example_1.py`](example_1.py))

```python
nums = [3, 1, 4]
nums.append(1)
nums.extend([5, 9])
nums.insert(0, 100)
print(nums)
nums.remove(1)       # removes the first 1 only
last = nums.pop()
first = nums.pop(0)
print(nums, "popped:", last, first)
```

### Example 2: Sorting  ([`example_2.py`](example_2.py))

```python
scores = [88, 42, 95, 67, 73]
print(sorted(scores))            # new list
print(scores)                    # unchanged
scores.sort(reverse=True)        # in place
print(scores)
words = ["banana", "Apple", "cherry", "kiwi"]
print(sorted(words, key=str.lower))
print(sorted(words, key=len))
```

### Example 3: Stack and queue with lists  ([`example_3.py`](example_3.py))

```python
stack = []
for item in ["a", "b", "c"]:
    stack.append(item)
print("Stack pop order:", stack.pop(), stack.pop(), stack.pop())

tasks = ["t1", "t2", "t3"]
print("index of t2:", tasks.index("t2"))
print("count of t1:", tasks.count("t1"))
tasks.reverse()
print(tasks)
# For real queues use collections.deque (Level 2)
```

## Practice

1. Remove all duplicates from a list while keeping the original order.
2. Sort a list of names by their last letter.
3. Write an undo feature using a list as a stack.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

# Day 031 · Mutable vs Immutable and Copying

_Beginner_

## Mutable vs immutable
| Immutable (can't change) | Mutable (can change) |
|--------------------------|----------------------|
| int, float, bool, str, tuple, frozenset, bytes | list, dict, set, bytearray, most custom objects |

When you "change" an immutable value, Python actually creates a **new object**.

## Python passes object references
A function receives a **reference to the same object**. If the object is mutable and the function changes it, the caller sees the change.

## Shallow vs deep copy
- **Shallow copy** (`copy.copy`, `lst.copy()`, `lst[:]`): makes a new outer container, but the inner objects are **shared**.
- **Deep copy** (`copy.deepcopy`): copies everything, all the way down.

## Examples

### Example 1: Immutable creates new objects  ([`example_1.py`](example_1.py))

```python
s = "hi"
print(id(s))
s += "!"
print(id(s), "(new object)")
lst = [1, 2]
print(id(lst))
lst += [3]
print(id(lst), "(same object, changed in place)")
```

### Example 2: Functions can change mutable arguments  ([`example_2.py`](example_2.py))

```python
def add_item(cart, item):
    cart.append(item)

def change_number(n):
    n += 100
    return n

my_cart = ["milk"]
add_item(my_cart, "bread")
print(my_cart)          # changed!

x = 5
change_number(x)
print(x)                # unchanged: ints are immutable
```

### Example 3: Shallow vs deep copy  ([`example_3.py`](example_3.py))

```python
import copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0].append(99)
print("original:", original)
print("shallow :", shallow, "<- inner list is shared")
print("deep    :", deep, "<- fully independent")
```

## Practice

1. Predict the output: `a = [[0]*2]*2; a[0][0] = 1; print(a)`. Explain why.
2. Write a function that returns a changed copy of a list without touching the original.
3. Is a tuple containing a list truly immutable? Test it.

---

[⬅ Day 030](../Day-030-Classic-List-and-Dictionary-Programs/README.md) · [🏠 Home](../README.md) · [Day 032 ➡](../Day-032-Docstrings-and-PEP-8-Writing-Clean-Code/README.md)

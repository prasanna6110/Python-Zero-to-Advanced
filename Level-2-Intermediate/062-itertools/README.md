# 062 · itertools

## Fast, memory-efficient iterator building blocks
| Function | What it does |
|----------|--------------|
| `count(start, step)` | counts forever |
| `cycle(it)` | repeats an iterable forever |
| `repeat(x, n)` | x, n times |
| `chain(a, b)` / `chain.from_iterable` | joins iterables together |
| `islice(it, start, stop)` | slices any iterator |
| `accumulate(it, func)` | running totals |
| `groupby(it, key)` | groups **consecutive** items (sort first!) |
| `product, permutations, combinations, combinations_with_replacement` | combinatorics |
| `zip_longest` | zip, padding the shorter iterable |
| `takewhile, dropwhile, filterfalse, compress, starmap, tee` | filtering and mapping |
| `pairwise` (3.10+), `batched` (3.12+) | windows and chunks |

## Examples

### Example 1: Infinite iterators and islice  ([`example_1.py`](example_1.py))

```python
from itertools import count, cycle, repeat, islice

print(list(islice(count(10, 5), 5)))
print(list(islice(cycle("ABC"), 7)))
print(list(repeat("hi", 3)))
for turn, player in zip(range(1, 6), cycle(["Asha", "Ravi"])):
    print(f"Turn {turn}: {player}")
```

### Example 2: Combinatorics  ([`example_2.py`](example_2.py))

```python
from itertools import product, permutations, combinations

print(list(product("AB", [1, 2])))
print(list(permutations("ABC", 2)))
print(list(combinations([1, 2, 3, 4], 2)))
pins = ["".join(p) for p in product("01", repeat=3)]
print("All 3-bit strings:", pins)
team = ["Asha", "Ravi", "Meera", "Kiran"]
print("Pairs for a project:", len(list(combinations(team, 2))))
```

### Example 3: groupby, accumulate, chain, pairwise, batched  ([`example_3.py`](example_3.py))

```python
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
```

## Practice

1. Generate every possible 4-letter arrangement of "ABCD".
2. Group a sorted list of students by grade with `groupby`.
3. Find all the ways to make ₹10 from ₹1, ₹2 and ₹5 coins using `product` or `combinations_with_replacement`.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

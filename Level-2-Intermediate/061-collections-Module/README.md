# 061 · collections Module

## Specialised containers
| Class | Use |
|-------|-----|
| `Counter` | counts things; `most_common()` |
| `defaultdict` | a dict that creates a default value for missing keys |
| `deque` | a double-ended queue: fast append and pop at both ends |
| `namedtuple` | a tuple with named fields |
| `OrderedDict` | a dict with `move_to_end` and `popitem(last=)` |
| `ChainMap` | several dicts viewed as one (lookups check each in turn) |

`deque(maxlen=n)` makes a **sliding window**: old items drop off automatically.

## Examples

### Example 1: Counter and defaultdict  ([`example_1.py`](example_1.py))

```python
from collections import Counter, defaultdict

words = "to be or not to be that is the question to be".split()
c = Counter(words)
print(c.most_common(3))
print(Counter("mississippi"))
print(Counter(a=3, b=1) + Counter(a=1, b=2))

by_letter = defaultdict(list)
for w in words:
    by_letter[w[0]].append(w)
print(dict(by_letter))
graph = defaultdict(set)
graph["A"].add("B")
print(graph)
```

### Example 2: deque as a queue and a sliding window  ([`example_2.py`](example_2.py))

```python
from collections import deque

q = deque(["t1", "t2"])
q.append("t3")
q.appendleft("urgent")
print(q.popleft(), q.popleft(), q)
q.rotate(1)
print(q)

recent = deque(maxlen=3)
for page in ["home", "about", "blog", "contact", "faq"]:
    recent.append(page)
    print("recent pages:", list(recent))
```

### Example 3: namedtuple, OrderedDict and ChainMap  ([`example_3.py`](example_3.py))

```python
from collections import namedtuple, OrderedDict, ChainMap

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p, p.x, p[1], p._asdict(), p._replace(x=10))

cache = OrderedDict()
for key in ["a", "b", "c"]:
    cache[key] = key.upper()
cache.move_to_end("a")                 # mark as recently used
cache.popitem(last=False)              # evict the oldest
print(cache)

defaults = {"theme": "light", "lang": "en"}
user = {"theme": "dark"}
settings = ChainMap(user, defaults)
print(settings["theme"], settings["lang"])
```

## Practice

1. Find the 5 most common words in a paragraph.
2. Build an LRU cache of size 3 using `OrderedDict`.
3. Use a `deque` to check for palindromes.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

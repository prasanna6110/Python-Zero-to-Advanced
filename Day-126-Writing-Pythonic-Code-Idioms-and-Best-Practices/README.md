# Day 126 · Writing Pythonic Code (Idioms and Best Practices)

_Ultra Advanced_

## "Pythonic" means using the language the way it was designed
| Instead of... | Write... |
|---------------|----------|
| `for i in range(len(lst)): lst[i]` | `for item in lst:` / `enumerate(lst)` |
| `if x == True:` | `if x:` |
| `if len(lst) == 0:` | `if not lst:` |
| `temp = a; a = b; b = temp` | `a, b = b, a` |
| `s = ""; for w in words: s += w` | `"".join(words)` |
| `d.has_key(k)` / try-except KeyError | `k in d`, `d.get(k, default)` |
| `f = open(...); ...; f.close()` | `with open(...) as f:` |
| `type(x) == int` | `isinstance(x, int)` |
| building a list just to loop over it once | a generator expression |
| `if x == 1 or x == 2 or x == 3` | `if x in {1, 2, 3}` |

## EAFP vs LBYL
- **EAFP** ("easier to ask forgiveness than permission"): `try` the thing and catch the exception. Python prefers this.
- **LBYL** ("look before you leap"): check first with `if`.

## The Zen of Python (`import this`)
Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Readability counts.

## Examples

### Example 1: Before and after: Pythonic rewrites  ([`example_1.py`](example_1.py))

```python
names = ["asha", "ravi", "meera"]
marks = [91, 78, 88]

# Non-Pythonic
result = []
for i in range(len(names)):
    if marks[i] > 80:
        result.append(names[i].upper())
print(result)

# Pythonic
print([n.upper() for n, m in zip(names, marks) if m > 80])

# Non-Pythonic
found = False
for n in names:
    if n == "ravi":
        found = True
# Pythonic
found = "ravi" in names
print(found, "| any above 90:", any(m > 90 for m in marks))
```

### Example 2: EAFP vs LBYL  ([`example_2.py`](example_2.py))

```python
config = {"host": "localhost"}

# LBYL
if "port" in config:
    port = config["port"]
else:
    port = 8000

# EAFP
try:
    port = config["port"]
except KeyError:
    port = 8000

# Best: a built-in made for exactly this
port = config.get("port", 8000)
print(port)

def to_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None
print([to_int(v) for v in ["5", "x", None, "42"]])
```

### Example 3: Handy idioms worth memorising  ([`example_3.py`](example_3.py))

```python
from collections import Counter, defaultdict

words = "the cat sat on the mat the end".split()
print(Counter(words).most_common(1))
groups = defaultdict(list)
for w in words:
    groups[len(w)].append(w)
print(dict(groups))
print(max(words, key=len), sorted(words, key=len)[:3])
print(dict(zip(["a", "b"], [1, 2])), {v: k for k, v in {"a": 1}.items()})
first, *_, last = words
print(first, last, "|", *reversed(words[:3]))
print(" ".join(f"{i}:{w}" for i, w in enumerate(words[:3], 1)))
with open(__file__) as f:
    print("this file has", sum(1 for _ in f), "lines")
```

## Practice

1. Take one of your old programs and rewrite it in Pythonic style.
2. Run `import this` and explain 5 of the lines in your own words.
3. Convert 3 LBYL snippets to EAFP.

---

[⬅ Day 125](../Day-125-The-Python-Ecosystem-Roadmap/README.md) · [🏠 Home](../README.md) · [Day 127 ➡](../Day-127-Common-Mistakes-and-Gotchas/README.md)

# Day 028 · Dictionaries

_Beginner_

## Dictionaries
A collection of **key → value** pairs: `{"name": "Asha", "age": 21}`.

- Keys must be **unique and hashable** (str, int, tuple...). Values can be anything.
- Since Python 3.7, dicts **keep insertion order**.
- Looking up, adding and deleting by key is very fast.

## Methods
| Method | Purpose |
|--------|---------|
| `d[k]` | get (raises KeyError if missing) |
| `d.get(k, default)` | safe get |
| `d.setdefault(k, v)` | get, or set the key if it's missing |
| `d.update(other)` / `d \| other` | merge |
| `d.pop(k)`, `d.popitem()`, `del d[k]` | remove |
| `d.keys()`, `d.values()`, `d.items()` | views |
| `dict.fromkeys(keys, v)` | create from keys |

## Examples

### Example 1: CRUD on a dictionary  ([`example_1.py`](example_1.py))

```python
student = {"name": "Asha", "age": 21}
student["branch"] = "EE"           # create
print(student["name"])             # read
student["age"] = 22                # update
del student["branch"]              # delete
print(student)
print(student.get("cgpa", "N/A"))  # safe read
```

### Example 2: Word frequency counter  ([`example_2.py`](example_2.py))

```python
text = "the cat and the hat and the bat"
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
print(freq)
most = max(freq, key=freq.get)
print("Most common:", most, freq[most])
```

### Example 3: Nested dicts, merging and iterating  ([`example_3.py`](example_3.py))

```python
db = {
    "u1": {"name": "Ravi", "skills": ["python", "sql"]},
    "u2": {"name": "Meera", "skills": ["java"]},
}
db["u2"]["skills"].append("python")
for uid, info in db.items():
    print(uid, info["name"], ", ".join(info["skills"]))

defaults = {"theme": "light", "lang": "en"}
user_prefs = {"theme": "dark"}
print(defaults | user_prefs)       # Python 3.9+ merge
print(dict.fromkeys(["a", "b"], 0))
```

## Practice

1. Build a phone book: add, search, delete and list contacts.
2. Invert a dictionary (swap keys and values).
3. Group words by their first letter into a dict of lists.

---

[⬅ Day 027](../Day-027-Sets/README.md) · [🏠 Home](../README.md) · [Day 029 ➡](../Day-029-Comprehensions-list-dict-and-set/README.md)

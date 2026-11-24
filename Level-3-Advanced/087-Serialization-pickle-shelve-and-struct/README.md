# 087 · Serialization: pickle, shelve and struct

## pickle
Turns **almost any Python object** into bytes and back again.
```python
pickle.dumps(obj) / pickle.loads(b)
pickle.dump(obj, f) / pickle.load(f)
```
⚠️ **Never unpickle data from an untrusted source.** Unpickling can run arbitrary code. Use JSON for data you exchange with others.

You can control what gets pickled with `__getstate__` and `__setstate__`.

## shelve
A persistent, **dict-like** store backed by pickle: `with shelve.open("db") as db: db["k"] = obj`

## struct
Packs and unpacks values into **C-style binary layouts**. It's used for binary file formats, network protocols and hardware.
```python
struct.pack("<I f", 7, 3.5)    # < little-endian, I uint32, f float
```

## Examples

### Example 1: pickle round trip  ([`example_1.py`](example_1.py))

```python
import pickle
from datetime import datetime

class Session:
    def __init__(self, user):
        self.user = user
        self.started = datetime(2026, 11, 24, 10, 0)
        self.cart = {"laptop": 1}

s = Session("prasanna")
data = pickle.dumps(s)
print(type(data), len(data), "bytes")
restored = pickle.loads(data)
print(restored.user, restored.started, restored.cart)

with open("session.pkl", "wb") as f:
    pickle.dump([s, {1, 2, 3}, (4, 5)], f)
with open("session.pkl", "rb") as f:
    print(pickle.load(f)[1:])
import os; os.remove("session.pkl")
```

### Example 2: __getstate__/__setstate__ and shelve  ([`example_2.py`](example_2.py))

```python
import pickle, shelve, glob, os

class Connection:
    def __init__(self, host):
        self.host = host
        self.socket = object()          # can't be pickled meaningfully
    def __getstate__(self):
        state = self.__dict__.copy()
        del state["socket"]
        return state
    def __setstate__(self, state):
        self.__dict__.update(state)
        self.socket = "reconnected"

c = pickle.loads(pickle.dumps(Connection("db.local")))
print(c.host, c.socket)

with shelve.open("mydb") as db:
    db["users"] = ["asha", "ravi"]
    db["config"] = {"theme": "dark"}
with shelve.open("mydb") as db:
    print(dict(db))
for f in glob.glob("mydb*"):
    os.remove(f)
```

### Example 3: struct for binary formats  ([`example_3.py`](example_3.py))

```python
import struct

# A record: id (uint16), temperature (float32), active (bool), code (4 bytes)
fmt = "<H f ? 4s"
packed = struct.pack(fmt, 101, 36.6, True, b"EE01")
print(packed, "size:", struct.calcsize(fmt))
rid, temp, active, code = struct.unpack(fmt, packed)
print(rid, round(temp, 1), active, code.decode())

# Reading a fake BMP-like header
header = struct.pack("<2sIHHI", b"BM", 1024, 0, 0, 54)
magic, size, _, _, offset = struct.unpack("<2sIHHI", header)
print(magic, size, offset)
print("big-endian 1:", struct.pack(">I", 1), "little-endian 1:", struct.pack("<I", 1))
```

## Practice

1. Save and load a game state (player, level, inventory) with pickle.
2. Build a persistent to-do list with shelve.
3. Write and read a binary file of 100 sensor readings using struct.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

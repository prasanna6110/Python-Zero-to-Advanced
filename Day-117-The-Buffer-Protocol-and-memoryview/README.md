# Day 117 · The Buffer Protocol and memoryview

_Ultra Advanced_

## The buffer protocol
Lets objects **share raw memory without copying it**. `bytes`, `bytearray`, `array.array`, `mmap`, NumPy arrays and others support it.

## memoryview
A **zero-copy view** onto the memory of a buffer object.
```python
mv = memoryview(bytearray(b"hello"))
mv[0] = ord("H")      # changes the original
mv[1:3]               # slicing doesn't copy!
```
- `mv.cast("I")` reinterprets the bytes as another type (for example uint32).
- You can inspect `mv.format`, `mv.itemsize`, `mv.shape`, `mv.nbytes` and `mv.readonly`.
- `mv.tobytes()` and `mv.tolist()` make copies when you need them.

## Why it matters
Fast binary parsing, network buffers (`sock.recv_into`), image and audio processing, and big data files.

`mmap` maps a file straight into memory, so you can work with huge files as though they were bytes.

## Examples

### Example 1: Zero-copy slicing vs copying  ([`example_1.py`](example_1.py))

```python
import time

data = bytearray(50_000_000)          # 50 MB

start = time.perf_counter()
for _ in range(20):
    chunk = data[10:40_000_000]       # copies 40 MB every time
copy_time = time.perf_counter() - start

mv = memoryview(data)
start = time.perf_counter()
for _ in range(20):
    chunk = mv[10:40_000_000]         # no copy
view_time = time.perf_counter() - start
print(f"bytearray slice: {copy_time:.3f}s | memoryview slice: {view_time:.6f}s")
```

### Example 2: Changing memory in place and casting  ([`example_2.py`](example_2.py))

```python
from array import array

buf = bytearray(b"hello world")
mv = memoryview(buf)
mv[0] = ord("H")
mv[6:11] = b"WORLD"
print(buf)

numbers = array("i", [1, 2, 3, 4])
mv = memoryview(numbers)
print("format:", mv.format, "itemsize:", mv.itemsize, "nbytes:", mv.nbytes)
raw = mv.cast("B")                    # view the same memory as bytes
print("raw bytes:", raw.tolist()[:8], "...")
raw[0] = 99                           # changes the int array!
print("numbers now:", numbers.tolist())

grid = memoryview(bytearray(range(12))).cast("B", shape=[3, 4])
print("2D view:", grid.tolist(), "| element [1][2]:", grid[1, 2])
```

### Example 3: mmap and recv_into  ([`example_3.py`](example_3.py))

```python
import mmap, os, socket

with open("big.bin", "wb") as f:
    f.write(b"HEADER" + b"." * 1000 + b"FOOTER")
with open("big.bin", "r+b") as f, mmap.mmap(f.fileno(), 0) as mm:
    print("first 6:", mm[:6], "| last 6:", mm[-6:])
    print("find FOOTER at:", mm.find(b"FOOTER"))
    mm[0:6] = b"header"                       # write straight to the file
with open("big.bin", "rb") as f:
    print("file now starts with:", f.read(6))
os.remove("big.bin")

a, b = socket.socketpair()
a.sendall(b"zero-copy network read")
buffer = bytearray(64)
n = b.recv_into(memoryview(buffer))           # no temporary bytes object
print("received:", buffer[:n])
a.close(); b.close()
```

## Practice

1. Parse a binary file of 1 million uint32 values using `memoryview.cast("I")`.
2. Count the newlines in a large file using mmap.
3. Implement a ring buffer on top of a bytearray and a memoryview.

---

[⬅ Day 116](../Day-116-ctypes-Calling-C-from-Python/README.md) · [🏠 Home](../README.md) · [Day 118 ➡](../Day-118-Mocking-and-Monkey-Patching-unittest-mock/README.md)

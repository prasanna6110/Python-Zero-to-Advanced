# 103 · ctypes: Calling C from Python

## ctypes
It loads shared libraries (`.so`, `.dll`, `.dylib`) and calls their C functions **directly**, with no compiling needed.

## Basics
```python
import ctypes, ctypes.util
libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.strlen.argtypes = [ctypes.c_char_p]
libc.strlen.restype = ctypes.c_size_t
```
| C type | ctypes |
|--------|--------|
| `int`, `double`, `char*` | `c_int`, `c_double`, `c_char_p` |
| pointer | `POINTER(T)`, `byref(x)`, `pointer(x)` |
| struct | subclass `ctypes.Structure` with `_fields_` |
| array | `(c_int * 5)()` |
| callback | `CFUNCTYPE(ret, *args)` |

**Always set `argtypes` and `restype`**. Getting them wrong can crash the interpreter.

## Other ways to speed up or interface with C
**cffi**, **Cython**, **pybind11**, **Rust + PyO3**, and the C API (writing `PyModuleDef` extension modules).

## Examples

### Example 1: Calling the C standard library  ([`example_1.py`](example_1.py))

```python
import ctypes, ctypes.util, sys

if sys.platform == "win32":
    libc = ctypes.cdll.msvcrt
else:
    libc = ctypes.CDLL(ctypes.util.find_library("c"))

libc.strlen.argtypes = [ctypes.c_char_p]
libc.strlen.restype = ctypes.c_size_t
print("strlen:", libc.strlen(b"Hello from C"))

libc.abs.argtypes = [ctypes.c_int]
libc.abs.restype = ctypes.c_int
print("abs:", libc.abs(-42))

buf = ctypes.create_string_buffer(32)
libc.sprintf(buf, b"%d + %d = %d", 2, 3, 5)
print("sprintf:", buf.value.decode())
```

### Example 2: Structures, arrays and pointers  ([`example_2.py`](example_2.py))

```python
import ctypes

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

class Rect(ctypes.Structure):
    _fields_ = [("top_left", Point), ("bottom_right", Point)]

r = Rect(Point(0, 10), Point(20, 0))
print("rect width:", r.bottom_right.x - r.top_left.x, "| size:", ctypes.sizeof(r), "bytes")

IntArray5 = ctypes.c_int * 5
arr = IntArray5(5, 3, 8, 1, 9)
print("array:", list(arr))

value = ctypes.c_double(3.14)
ptr = ctypes.pointer(value)
ptr.contents.value = 2.71              # change it through the pointer
print("changed through pointer:", value.value)
print("address:", hex(ctypes.addressof(value)))
```

### Example 3: Passing a Python callback to C (qsort)  ([`example_3.py`](example_3.py))

```python
import ctypes, ctypes.util, sys

libc = ctypes.cdll.msvcrt if sys.platform == "win32" else ctypes.CDLL(ctypes.util.find_library("c"))

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

def py_compare(a, b):
    return a[0] - b[0]                 # ascending order

nums = (ctypes.c_int * 8)(42, 7, 19, 3, 88, 1, 56, 23)
libc.qsort(nums, len(nums), ctypes.sizeof(ctypes.c_int), CMPFUNC(py_compare))
print("sorted by C's qsort with a Python comparator:", list(nums))
```

## Practice

1. Call `time()` from libc and compare it with `time.time()`.
2. Write a tiny C library with `gcc -shared -fPIC mylib.c -o mylib.so`, then call it from Python.
3. Build a ctypes Structure that matches a binary file header.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

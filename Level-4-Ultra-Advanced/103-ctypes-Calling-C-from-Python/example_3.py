# 103 · ctypes: Calling C from Python — Example 3: Passing a Python callback to C (qsort)
# Run: python example_3.py

import ctypes, ctypes.util, sys

libc = ctypes.cdll.msvcrt if sys.platform == "win32" else ctypes.CDLL(ctypes.util.find_library("c"))

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

def py_compare(a, b):
    return a[0] - b[0]                 # ascending order

nums = (ctypes.c_int * 8)(42, 7, 19, 3, 88, 1, 56, 23)
libc.qsort(nums, len(nums), ctypes.sizeof(ctypes.c_int), CMPFUNC(py_compare))
print("sorted by C's qsort with a Python comparator:", list(nums))

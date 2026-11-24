# Day 116 · ctypes: Calling C from Python — Structures, arrays and pointers
# Run: python example_2.py

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

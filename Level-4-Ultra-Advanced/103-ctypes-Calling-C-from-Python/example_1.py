# 103 · ctypes: Calling C from Python — Example 1: Calling the C standard library
# Run: python example_1.py

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

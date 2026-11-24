# Day 097 · Serialization: pickle, shelve and struct — struct for binary formats
# Run: python example_3.py

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

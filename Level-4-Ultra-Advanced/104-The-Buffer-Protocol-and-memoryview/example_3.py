# 104 · The Buffer Protocol and memoryview — Example 3: mmap and recv_into
# Run: python example_3.py

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

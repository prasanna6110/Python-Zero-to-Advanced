# Day 117 · The Buffer Protocol and memoryview — Changing memory in place and casting
# Run: python example_2.py

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

# 051 · Context Managers (with and contextlib) — Example 3: suppress, redirect_stdout and ExitStack
# Run: python example_3.py

from contextlib import suppress, redirect_stdout, ExitStack
import io, os

with suppress(FileNotFoundError):
    os.remove("no_such_file.txt")
print("No crash thanks to suppress")

buffer = io.StringIO()
with redirect_stdout(buffer):
    print("this goes into the buffer")
print("Captured:", buffer.getvalue().strip())

names = ["f1.txt", "f2.txt", "f3.txt"]
with ExitStack() as stack:
    files = [stack.enter_context(open(n, "w")) for n in names]
    for i, f in enumerate(files):
        f.write(f"file {i}")
print("all closed:", all(f.closed for f in files))
for n in names:
    os.remove(n)

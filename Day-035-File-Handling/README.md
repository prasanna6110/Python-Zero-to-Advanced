# Day 035 · File Handling

_Beginner_

## Opening files
`open(path, mode, encoding="utf-8")`

| Mode | Meaning |
|------|---------|
| `"r"` | read (the default; the file must exist) |
| `"w"` | write (creates the file or **erases** it) |
| `"a"` | append |
| `"x"` | create (fails if the file already exists) |
| `"b"` | binary (`"rb"`, `"wb"`) |
| `"+"` | read and write |

## Always use `with`
`with open(...) as f:` **closes the file automatically**, even if an error happens.

## Reading
- `f.read()` reads the whole file.
- `f.readline()` reads one line.
- `f.readlines()` returns a list of lines.
- `for line in f:` reads line by line and uses little memory, which makes it the best choice for big files.

## Other operations
- `f.write(s)` and `f.writelines(list)`.
- `f.seek(pos)` and `f.tell()` move and report your position in the file.

## Examples

### Example 1: Write, append, read  ([`example_1.py`](example_1.py))

```python
import os
path = "demo_notes.txt"
with open(path, "w", encoding="utf-8") as f:
    f.write("Line 1: Python\n")
    f.write("Line 2: Files\n")
with open(path, "a", encoding="utf-8") as f:
    f.write("Line 3: Appended\n")
with open(path, encoding="utf-8") as f:
    print(f.read())
os.remove(path)    # clean up
```

### Example 2: Processing a file line by line  ([`example_2.py`](example_2.py))

```python
import os
path = "marks.txt"
with open(path, "w") as f:
    f.writelines(["Asha,91\n", "Ravi,78\n", "Meera,85\n"])

total = count = 0
with open(path) as f:
    for line in f:
        name, mark = line.strip().split(",")
        total += int(mark)
        count += 1
        print(f"{name:<6} {mark}")
print("Average:", total / count)
os.remove(path)
```

### Example 3: Binary files, seek and tell  ([`example_3.py`](example_3.py))

```python
import os
path = "data.bin"
with open(path, "wb") as f:
    f.write(bytes([72, 101, 108, 108, 111]))   # "Hello"
with open(path, "rb") as f:
    print(f.read())
    f.seek(1)
    print("tell:", f.tell(), "next 3 bytes:", f.read(3))
try:
    open("does_not_exist.txt")
except FileNotFoundError as e:
    print("Handled:", e.strerror)
os.remove(path)
```

## Practice

1. Count the lines, words and characters in a text file.
2. Copy one file to another, line by line.
3. Make a simple diary app that appends dated entries to a file.

---

[⬅ Day 034](../Day-034-Raising-Exceptions-and-Custom-Exceptions/README.md) · [🏠 Home](../README.md) · [Day 036 ➡](../Day-036-Modules-Imports-and-name/README.md)

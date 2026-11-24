# Day 065 · os, shutil and pathlib

_Intermediate_

## pathlib: the modern, object-oriented way to work with paths
```python
from pathlib import Path
p = Path("folder") / "file.txt"
```
`p.name, p.stem, p.suffix, p.parent, p.exists(), p.is_file(), p.is_dir(), p.mkdir(parents=True, exist_ok=True), p.read_text(), p.write_text(), p.glob("*.py"), p.rglob("*"), p.iterdir(), p.unlink(), p.rename()`

## os
`os.getcwd(), os.listdir(), os.environ, os.getenv("HOME"), os.walk(), os.path.join(), os.cpu_count()`

## shutil: high-level file operations
`copy, copy2, copytree, move, rmtree, make_archive, disk_usage`

Prefer **pathlib** in new code. It works the same way on Windows, Mac and Linux.

## Examples

### Example 1: pathlib basics  ([`example_1.py`](example_1.py))

```python
from pathlib import Path

p = Path("projects") / "app" / "main.py"
print(p, "|", p.name, "|", p.stem, "|", p.suffix, "|", p.parent)
print(p.with_suffix(".txt"), p.parts)
print("home:", Path.home().exists(), "cwd is dir:", Path.cwd().is_dir())
```

### Example 2: Creating, listing and globbing files  ([`example_2.py`](example_2.py))

```python
from pathlib import Path
import shutil

base = Path("demo_dir")
(base / "src").mkdir(parents=True, exist_ok=True)
for name in ["a.py", "b.py", "notes.txt"]:
    (base / "src" / name).write_text(f"# {name}\n")
print([f.name for f in (base / "src").iterdir()])
print("Python files:", [f.name for f in base.rglob("*.py")])
print("size of a.py:", (base / "src" / "a.py").stat().st_size, "bytes")
shutil.rmtree(base)
print("cleaned up:", not base.exists())
```

### Example 3: os.walk, environment variables and organising files  ([`example_3.py`](example_3.py))

```python
import os, shutil
from pathlib import Path

root = Path("downloads_demo")
root.mkdir(exist_ok=True)
for f in ["song.mp3", "photo.jpg", "doc.pdf", "pic.png", "notes.pdf"]:
    (root / f).touch()

types = {".mp3": "Music", ".jpg": "Images", ".png": "Images", ".pdf": "Documents"}
for file in list(root.iterdir()):
    folder = root / types.get(file.suffix, "Other")
    folder.mkdir(exist_ok=True)
    shutil.move(str(file), folder / file.name)

for dirpath, dirnames, filenames in os.walk(root):
    print(dirpath, filenames)
print("PATH has", len(os.environ.get("PATH", "").split(os.pathsep)), "entries;",
      "CPUs:", os.cpu_count())
shutil.rmtree(root)
```

## Practice

1. Write a script that lists the 5 biggest files in a folder.
2. Write a file organiser that sorts files into folders by extension.
3. Find every `.py` file in a project and count the total number of lines.

---

[⬅ Day 064](../Day-064-math-random-and-statistics/README.md) · [🏠 Home](../README.md) · [Day 066 ➡](../Day-066-ZIP-Archives-and-Temporary-Files/README.md)

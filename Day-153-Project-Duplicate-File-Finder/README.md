# Day 153 · Project: Duplicate File Finder

_Projects_

**Concepts:** `os.walk` / `rglob`, **hashing** files in chunks, grouping by size first (a speed trick), `defaultdict`, human-readable sizes.

It finds files with the same content (even when their names differ) and shows how much space you could free up.

## Code

### Duplicate File Finder  ([`main.py`](main.py))

```python
import hashlib
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

DEMO = not sys.stdin.isatty()

def human(n):
    for unit in ["B", "KB", "MB", "GB"]:
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} TB"

def file_hash(path, chunk=1 << 16):
    h = hashlib.blake2b()
    with open(path, "rb") as f:
        while block := f.read(chunk):
            h.update(block)
    return h.hexdigest()

def find_duplicates(root):
    by_size = defaultdict(list)
    for p in Path(root).rglob("*"):
        if p.is_file():
            by_size[p.stat().st_size].append(p)
    by_hash = defaultdict(list)
    hashed = 0
    for size, files in by_size.items():
        if len(files) < 2:                     # a file with a unique size can't have a duplicate
            continue
        for f in files:
            by_hash[(size, file_hash(f))].append(f); hashed += 1
    print(f"Scanned {sum(map(len, by_size.values()))} files, hashed only {hashed} of them")
    return [sorted(g) for g in by_hash.values() if len(g) > 1]

def report(groups, root):
    wasted = 0
    for i, g in enumerate(groups, 1):
        size = g[0].stat().st_size
        wasted += size * (len(g) - 1)
        print(f"\nGroup {i} ({human(size)} each):")
        for f in g:
            print("   ", f.relative_to(root))
    print(f"\n🧹 You could free {human(wasted)} by deleting the duplicates.")

if __name__ == "__main__":
    if DEMO:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "photos").mkdir(); (root / "backup").mkdir()
            img = b"\x89PNG" + bytes(range(256)) * 400
            (root / "photos" / "trip.png").write_bytes(img)
            (root / "backup" / "trip_copy.png").write_bytes(img)
            (root / "backup" / "IMG_001.png").write_bytes(img)
            (root / "notes.txt").write_text("Python notes")
            (root / "backup" / "notes_old.txt").write_text("Python notes")
            (root / "other.txt").write_text("Python notez")           # same size, different content
            report(find_duplicates(root), root)
    else:
        root = Path(input("Folder to scan: ").strip('" ')).expanduser()
        report(find_duplicates(root), root)
```

## Extend this project

1. Add an option to delete the duplicates safely (move them to a `_duplicates` folder).
2. Find *similar* images using a perceptual hash (the `imagehash` library).
3. Show a progress bar while scanning.

---

[⬅ Day 152](../Day-152-Project-Smart-File-Organizer/README.md) · [🏠 Home](../README.md) · [Day 154 ➡](../Day-154-Project-Log-File-Analyzer/README.md)

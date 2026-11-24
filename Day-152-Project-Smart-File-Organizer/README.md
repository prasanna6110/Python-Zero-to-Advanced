# Day 152 · Project: Smart File Organizer

_Projects_

**Concepts:** `pathlib`, `shutil.move`, mapping file types to folders, handling duplicate names, a dry-run mode, an **undo log**.

It tidies a messy Downloads folder into Images, Documents, Videos, Code and so on, and can undo what it did.

## Code

### Smart File Organizer  ([`main.py`](main.py))

```python
import json
import shutil
import sys
import tempfile
from pathlib import Path

DEMO = not sys.stdin.isatty()
CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"},
    "Documents": {".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".csv"},
    "Videos": {".mp4", ".mkv", ".mov", ".avi"},
    "Audio": {".mp3", ".wav", ".flac"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Code": {".py", ".ipynb", ".js", ".html", ".css", ".c", ".cpp", ".java"},
}

def category_for(path):
    ext = path.suffix.lower()
    return next((cat for cat, exts in CATEGORIES.items() if ext in exts), "Others")

def unique_target(target):
    n = 1
    while target.exists():
        target = target.with_name(f"{target.stem} ({n}){target.suffix}")
        n += 1
    return target

def organize(folder, dry_run=False):
    moves = []
    for f in sorted(p for p in folder.iterdir() if p.is_file() and p.name != ".organizer_log.json"):
        dest_dir = folder / category_for(f)
        target = unique_target(dest_dir / f.name)
        moves.append((str(f), str(target)))
        print(f"{'[dry-run] ' if dry_run else ''}{f.name:<28} -> {dest_dir.name}/{target.name}")
        if not dry_run:
            dest_dir.mkdir(exist_ok=True)
            shutil.move(str(f), target)
    if not dry_run:
        (folder / ".organizer_log.json").write_text(json.dumps(moves))
    return moves

def undo(folder):
    log = folder / ".organizer_log.json"
    for src, dst in reversed(json.loads(log.read_text())):
        shutil.move(dst, src)
    for d in folder.iterdir():
        if d.is_dir() and not any(d.iterdir()):
            d.rmdir()
    log.unlink()
    print("↩️  Undo complete")

def summary(folder):
    for d in sorted(p for p in folder.iterdir() if p.is_dir()):
        files = list(d.iterdir())
        print(f"  📁 {d.name:<10} {len(files)} files, {sum(f.stat().st_size for f in files)} bytes")

if __name__ == "__main__":
    if DEMO:
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            for name in ["holiday.jpg", "resume.pdf", "notes.txt", "song.mp3", "project.zip", "main.py",
                         "lecture.mp4", "Holiday.JPG", "data.csv", "unknown.xyz", "notes (copy).txt"]:
                (folder / name).write_text("x" * len(name))
            (folder / "Images").mkdir(); (folder / "Images" / "holiday.jpg").write_text("existing")
            organize(folder, dry_run=True)
            print()
            organize(folder)
            summary(folder)
            undo(folder)
            print("Back to:", sorted(p.name for p in folder.iterdir() if p.is_file())[:5], "...")
    else:
        folder = Path(input("Folder to organize: ").strip('" ')).expanduser()
        organize(folder, dry_run=True)
        if input("Proceed? (y/n) ").lower() == "y":
            organize(folder); summary(folder)
            if input("Undo? (y/n) ").lower() == "y":
                undo(folder)
```

## Extend this project

1. Also sort files by date into `2026/11/` folders.
2. Watch the folder and organise new files automatically (poll every 5 seconds).
3. Read the categories from a JSON config file.

---

[⬅ Day 151](../Day-151-Project-Inventory-Management-System-SQLite/README.md) · [🏠 Home](../README.md) · [Day 153 ➡](../Day-153-Project-Duplicate-File-Finder/README.md)

# Day 065 · os, shutil and pathlib — os.walk, environment variables and organising files
# Run: python example_3.py

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

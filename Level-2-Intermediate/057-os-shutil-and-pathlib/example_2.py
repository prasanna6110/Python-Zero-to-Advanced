# 057 · os, shutil and pathlib — Example 2: Creating, listing and globbing files
# Run: python example_2.py

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

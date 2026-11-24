# 057 · os, shutil and pathlib — Example 1: pathlib basics
# Run: python example_1.py

from pathlib import Path

p = Path("projects") / "app" / "main.py"
print(p, "|", p.name, "|", p.stem, "|", p.suffix, "|", p.parent)
print(p.with_suffix(".txt"), p.parts)
print("home:", Path.home().exists(), "cwd is dir:", Path.cwd().is_dir())

# 084 · Packaging and Distributing Your Code — Example 1: Generating a package skeleton
# Run: python example_1.py

from pathlib import Path
import shutil

name = "greetkit"
root = Path(f"{name}-project")
files = {
    "pyproject.toml": f'''[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "{name}"
version = "0.1.0"
description = "Tiny greeting library"
authors = [{{name = "Prasanna Kumar Pandey"}}]
requires-python = ">=3.10"

[project.scripts]
greet = "{name}.core:main"
''',
    f"src/{name}/__init__.py": 'from .core import greet\n__version__ = "0.1.0"\n',
    f"src/{name}/core.py": 'def greet(n): return f"Hello, {n}!"\ndef main(): print(greet("World"))\n',
    "tests/test_core.py": f"from {name} import greet\ndef test_greet(): assert greet('A') == 'Hello, A!'\n",
    "README.md": f"# {name}\n",
}
for rel, content in files.items():
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)
for p in sorted(root.rglob("*")):
    print("  " * (len(p.relative_to(root).parts) - 1) + p.name)
shutil.rmtree(root)

# Day 094 · Packaging and Distributing Your Code

_Advanced_

## A modern project layout (the src layout)
```
my-package/
├── pyproject.toml
├── README.md
├── LICENSE
├── src/
│   └── mypkg/
│       ├── __init__.py
│       └── core.py
└── tests/
    └── test_core.py
```
## pyproject.toml (PEP 621)
```toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "mypkg"
version = "0.1.0"
dependencies = ["requests>=2"]

[project.scripts]
mypkg = "mypkg.core:main"     # creates a terminal command
```
## Build and publish
```bash
pip install build twine
python -m build              # creates dist/*.whl and *.tar.gz
twine upload dist/*          # publish to PyPI
pip install -e .             # editable install while you develop
```
Other tools you'll meet: **uv**, **poetry**, **hatch**, **pdm**.

## Examples

### Example 1: Generating a package skeleton  ([`example_1.py`](example_1.py))

```python
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
```

### Example 2: Version and metadata inside a package  ([`example_2.py`](example_2.py))

```python
import importlib.metadata as md

def show(pkg):
    try:
        meta = md.metadata(pkg)
        print(f"{pkg} {md.version(pkg)} - {meta['Summary']}")
        eps = [ep.name for ep in md.entry_points(group="console_scripts") if ep.value.startswith(pkg)]
        print("  console scripts:", eps[:5])
    except md.PackageNotFoundError:
        print(f"{pkg}: not installed")

show("pip")
show("setuptools")
```

### Example 3: Building a wheel for real (when setuptools is available)  ([`example_3.py`](example_3.py))

```python
import subprocess, sys, shutil, importlib.util
from pathlib import Path

root = Path("mini_pkg")
(root / "src" / "mini").mkdir(parents=True, exist_ok=True)
(root / "src" / "mini" / "__init__.py").write_text("VALUE = 42\n")
(root / "pyproject.toml").write_text(
    '[build-system]\nrequires = ["setuptools"]\nbuild-backend = "setuptools.build_meta"\n'
    '[project]\nname = "mini"\nversion = "1.0"\n')

if importlib.util.find_spec("setuptools"):
    r = subprocess.run([sys.executable, "-m", "pip", "wheel", "--no-deps", "--no-build-isolation",
                        "-w", "dist", str(root)], capture_output=True, text=True)
    print("built:", [p.name for p in Path("dist").glob("*.whl")] if r.returncode == 0 else r.stderr[-300:])
else:
    print("setuptools not installed; run: pip install setuptools")
shutil.rmtree(root, ignore_errors=True)
shutil.rmtree("dist", ignore_errors=True)
```

## Practice

1. Turn one of your utilities into an installable package with `pip install -e .`.
2. Add a console script entry point and run it from the terminal.
3. Publish to **TestPyPI** (test.pypi.org) for practice.

---

[⬅ Day 093](../Day-093-Performance-Profiling-and-Optimisation/README.md) · [🏠 Home](../README.md) · [Day 095 ➡](../Day-095-Design-Patterns-in-Python/README.md)

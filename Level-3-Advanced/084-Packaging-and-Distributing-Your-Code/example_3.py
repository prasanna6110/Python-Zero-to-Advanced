# 084 · Packaging and Distributing Your Code — Example 3: Building a wheel for real (when setuptools is available)
# Run: python example_3.py

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

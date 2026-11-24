# Day 037 · Packages, pip and Virtual Environments — Checking installed packages from code
# Run: python example_2.py

from importlib import metadata

for pkg in ["pip", "setuptools", "requests"]:
    try:
        print(f"{pkg}: {metadata.version(pkg)}")
    except metadata.PackageNotFoundError:
        print(f"{pkg}: not installed  (run: pip install {pkg})")

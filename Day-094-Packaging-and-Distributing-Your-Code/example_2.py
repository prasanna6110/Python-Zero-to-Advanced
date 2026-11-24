# Day 094 · Packaging and Distributing Your Code — Version and metadata inside a package
# Run: python example_2.py

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

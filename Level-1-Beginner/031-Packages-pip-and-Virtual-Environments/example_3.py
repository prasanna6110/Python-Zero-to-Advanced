# 031 · Packages, pip and Virtual Environments — Example 3: Are we inside a virtual environment?
# Run: python example_3.py

import sys

in_venv = sys.prefix != sys.base_prefix
print("Inside virtual env:", in_venv)
print("sys.prefix:", sys.prefix)
print("Tip: create one with  python -m venv .venv")

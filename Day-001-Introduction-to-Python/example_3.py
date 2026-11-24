# Day 001 · Introduction to Python — Checking your Python version from code
# Run: python example_3.py

import sys
import platform

print("Python version:", sys.version.split()[0])
print("Running on:", platform.system())
print("Executable path:", sys.executable)

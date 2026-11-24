# Day 001 · Introduction to Python

_Beginner_

## What is Python?
Python is a **high-level, interpreted, general-purpose** programming language created in 1991. It is popular because:

- **Easy to read**: the code looks almost like English.
- **Interpreted**: the code runs line by line, so there is no separate compile step.
- **Dynamically typed**: you don't declare types; Python works them out.
- **Huge ecosystem**: web (Django, FastAPI), data science (NumPy, Pandas), AI/ML (PyTorch, TensorFlow), automation, scripting and more.

## Setup
1. Download Python from python.org (3.12 or newer).
2. Check the installation: `python --version` (or `python3 --version` on Mac/Linux).
3. Install an editor such as **VS Code** with the Python extension.

## Running Python
- **Script mode**: save code in `hello.py` and run `python hello.py`.
- **Interactive mode (REPL)**: type `python` in a terminal and run code line by line. Exit with `exit()`.

## Key points
- Indentation (spaces at the start of a line) is **part of the syntax** in Python. Use 4 spaces.
- Python is **case-sensitive**: `print` and `Print` are different.
- `print()` shows output on the screen.

## Examples

### Example 1: Your first program  ([`example_1.py`](example_1.py))

```python
print("Hello, World!")
print("Welcome to Python")
```

### Example 2: Python as a calculator  ([`example_2.py`](example_2.py))

```python
print(10 + 5)
print(10 * 5)
print(2 ** 10)      # power: 2 to the power 10
print(17 / 5)       # normal division gives a float
print(17 // 5)      # floor division gives an integer
```

### Example 3: Checking your Python version from code  ([`example_3.py`](example_3.py))

```python
import sys
import platform

print("Python version:", sys.version.split()[0])
print("Running on:", platform.system())
print("Executable path:", sys.executable)
```

## Practice

1. Print your name, your college and your favourite programming language on three separate lines.
2. Use Python as a calculator to find how many seconds there are in a year.
3. Open the REPL and try `import this`. Read "The Zen of Python".

---

[🏠 Home](../README.md) · [Day 002 ➡](../Day-002-print-Comments-and-Escape-Sequences/README.md)

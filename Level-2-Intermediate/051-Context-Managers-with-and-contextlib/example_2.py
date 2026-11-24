# 051 · Context Managers (with and contextlib) — Example 2: @contextmanager
# Run: python example_2.py

from contextlib import contextmanager
import os, tempfile

@contextmanager
def working_directory(path):
    old = os.getcwd()
    os.chdir(path)
    try:
        yield path
    finally:
        os.chdir(old)       # always restored

tmp = tempfile.gettempdir()
print("before:", os.getcwd() != tmp)
with working_directory(tmp) as p:
    print("inside:", os.path.samefile(os.getcwd(), p))
print("after restored:", os.getcwd() != tmp)

# Day 036 · Modules, Imports and __name__ — Creating and importing your own module
# Run: python example_2.py

import pathlib
import sys

# Create a module file on the fly (normally you write it by hand)
pathlib.Path("mytools.py").write_text(
    'PI = 3.14159\n'
    'def circle_area(r):\n'
    '    return PI * r * r\n'
    'if __name__ == "__main__":\n'
    '    print("mytools run directly")\n'
)
sys.path.insert(0, ".")
import mytools
print(mytools.circle_area(2))
print("module name:", mytools.__name__)
pathlib.Path("mytools.py").unlink()

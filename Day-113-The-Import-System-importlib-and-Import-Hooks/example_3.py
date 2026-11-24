# Day 113 · The Import System: importlib and Import Hooks — A custom import hook: modules from a dictionary
# Run: python example_3.py

import sys, importlib.abc, importlib.util

VIRTUAL_MODULES = {
    "virtual_math": "def triple(x):\n    return 3 * x\nPI = 3.14159\n",
    "virtual_greet": "from virtual_math import PI\ndef hi(n):\n    return f'Hi {n}, PI is {PI}'\n",
}

class DictFinder(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    def find_spec(self, fullname, path, target=None):
        if fullname in VIRTUAL_MODULES:
            return importlib.util.spec_from_loader(fullname, self, origin="memory")
        return None
    def create_module(self, spec):
        return None                         # use the default module object
    def exec_module(self, module):
        print(f"  [hook] loading {module.__name__} from memory")
        exec(VIRTUAL_MODULES[module.__name__], module.__dict__)

sys.meta_path.insert(0, DictFinder())
import virtual_greet
import virtual_math
print(virtual_greet.hi("Prasanna"), virtual_math.triple(7))
print(virtual_math.__spec__.origin)

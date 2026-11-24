# Day 113 · The Import System: importlib and Import Hooks

_Ultra Advanced_

## What `import x` does
1. Checks `sys.modules`, the **module cache**. If x is already there, it returns it.
2. Otherwise asks each **finder** in `sys.meta_path` for a **ModuleSpec**.
3. The spec's **loader** creates the module and runs (`exec_module`) its code.
4. Stores the module in `sys.modules` and binds the name.

## importlib tools
| Tool | Use |
|------|-----|
| `importlib.import_module("pkg.mod")` | import using a string name |
| `importlib.reload(mod)` | re-run a module's code |
| `importlib.util.spec_from_file_location` | import any file path |
| `importlib.util.LazyLoader` | lazy imports |
| `importlib.resources` | read data files shipped with a package |

## Custom hooks
Write a `MetaPathFinder` (with `find_spec`) and a `Loader` (with `create_module` and `exec_module`) to import code from anywhere: a database, a URL, encrypted files, or even other languages.

## Examples

### Example 1: Dynamic imports and the module cache  ([`example_1.py`](example_1.py))

```python
import importlib, sys

for name in ["json", "math", "statistics"]:
    mod = importlib.import_module(name)
    print(f"{name:<11} loaded from {getattr(mod, '__file__', 'built-in')}")
print("json in sys.modules:", "json" in sys.modules)
print("finders on sys.meta_path:", [type(f).__name__ if not isinstance(f, type) else f.__name__ for f in sys.meta_path])
import json
print("same object?", json is sys.modules["json"])
```

### Example 2: Importing from a file path and reloading  ([`example_2.py`](example_2.py))

```python
import importlib, importlib.util, pathlib, sys

path = pathlib.Path("settings_plugin.py")
path.write_text("VERSION = 1\ndef hello(): return 'v1'\n")
spec = importlib.util.spec_from_file_location("settings_plugin", path)
mod = importlib.util.module_from_spec(spec)
sys.modules["settings_plugin"] = mod
spec.loader.exec_module(mod)
print(mod.VERSION, mod.hello())

path.write_text("VERSION = 2\ndef hello(): return 'v2 (hot reloaded)'\n")
importlib.invalidate_caches()
mod = importlib.reload(mod)
print(mod.VERSION, mod.hello())
path.unlink()
```

### Example 3: A custom import hook: modules from a dictionary  ([`example_3.py`](example_3.py))

```python
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
```

## Practice

1. Write a hook that logs every module that gets imported, along with how long it took.
2. Write a loader that imports `.json` files as modules, where the JSON keys become attributes.
3. Use `importlib.util.LazyLoader` to delay loading a heavy module.

---

[⬅ Day 112](../Day-112-contextvars-Context-Local-State/README.md) · [🏠 Home](../README.md) · [Day 114 ➡](../Day-114-AST-Parsing-Analysing-and-Transforming-Code/README.md)

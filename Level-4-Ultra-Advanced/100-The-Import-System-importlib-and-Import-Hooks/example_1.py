# 100 · The Import System: importlib and Import Hooks — Example 1: Dynamic imports and the module cache
# Run: python example_1.py

import importlib, sys

for name in ["json", "math", "statistics"]:
    mod = importlib.import_module(name)
    print(f"{name:<11} loaded from {getattr(mod, '__file__', 'built-in')}")
print("json in sys.modules:", "json" in sys.modules)
print("finders on sys.meta_path:", [type(f).__name__ if not isinstance(f, type) else f.__name__ for f in sys.meta_path])
import json
print("same object?", json is sys.modules["json"])

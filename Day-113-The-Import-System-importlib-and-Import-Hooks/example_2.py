# Day 113 · The Import System: importlib and Import Hooks — Importing from a file path and reloading
# Run: python example_2.py

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

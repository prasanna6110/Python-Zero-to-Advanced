# 079 · The GIL and Choosing the Right Concurrency Model — Example 3: Inspecting the interpreter's GIL situation
# Run: python example_3.py

import sys, sysconfig

print("Python:", sys.version.split()[0])
gil_disabled_build = bool(sysconfig.get_config_var("Py_GIL_DISABLED"))
print("Free-threaded build:", gil_disabled_build)
if hasattr(sys, "_is_gil_enabled"):
    print("GIL currently enabled:", sys._is_gil_enabled())
print("Thread switch interval (s):", sys.getswitchinterval())

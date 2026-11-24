# 108 · Tracing, Profiling Hooks and Audit Hooks — Example 3: sys.excepthook, atexit and sys.monitoring
# Run: python example_3.py

import sys, atexit

def friendly_hook(exc_type, exc, tb):
    print(f"😅 Oops! {exc_type.__name__}: {exc}. (A custom excepthook handled this.)")

atexit.register(lambda: print("atexit: cleanup done, goodbye!"))

if hasattr(sys, "monitoring"):
    mon = sys.monitoring
    TOOL = mon.PROFILER_ID
    calls = {}
    def on_start(code, offset):
        calls[code.co_name] = calls.get(code.co_name, 0) + 1
    mon.use_tool_id(TOOL, "mini-profiler")
    mon.register_callback(TOOL, mon.events.PY_START, on_start)
    mon.set_events(TOOL, mon.events.PY_START)

    def square(x): return x * x
    def total(n): return sum(square(i) for i in range(n))
    total(5)
    mon.set_events(TOOL, 0)
    mon.free_tool_id(TOOL)
    print("sys.monitoring call counts:", {k: v for k, v in calls.items() if k in {"square", "total"}})

sys.excepthook = friendly_hook
# A real uncaught `raise RuntimeError(...)` would now print via friendly_hook (and exit with code 1).
# Here we call the hook ourselves so the example finishes cleanly:
try:
    raise RuntimeError("something unexpected")
except RuntimeError:
    sys.excepthook(*sys.exc_info())

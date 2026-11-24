# Day 121 · Tracing, Profiling Hooks and Audit Hooks

_Ultra Advanced_

## Interpreter hooks (how debuggers, profilers and coverage tools are built)
| Hook | Purpose |
|------|---------|
| `sys.settrace(func)` | called on every **call, line, return and exception**. pdb and coverage.py use it |
| `sys.setprofile(func)` | called on function calls and returns only (faster) |
| `sys.monitoring` (3.12+) | a new, low-overhead monitoring API (PEP 669) |
| `sys.addaudithook(func)` | sees security-sensitive events: `open`, `exec`, `socket.connect`, `subprocess.Popen`... (PEP 578) |
| `sys.excepthook` | a custom handler for uncaught exceptions |
| `sys.breakpointhook` | controls what `breakpoint()` does |
| `atexit.register(f)` | runs f when the interpreter exits |

⚠️ Trace functions slow the program down a lot, so only use them while debugging or for tools.

## Examples

### Example 1: Building a mini tracer and line coverage tool  ([`example_1.py`](example_1.py))

```python
import sys

def fizz(n):
    if n % 3 == 0:
        return "Fizz"
    return str(n)

executed = set()
def tracer(frame, event, arg):
    if frame.f_code.co_name == "fizz":
        if event == "call":
            print(f"call  fizz(n={frame.f_locals['n']})")
        elif event == "line":
            executed.add(frame.f_lineno)
        elif event == "return":
            print(f"return {arg!r}")
    return tracer

sys.settrace(tracer)
fizz(3); fizz(4)
sys.settrace(None)
first = fizz.__code__.co_firstlineno
print("lines executed (relative to the def):", sorted(l - first for l in executed))
```

### Example 2: Audit hooks: watching what code does  ([`example_2.py`](example_2.py))

```python
import sys, os, tempfile

seen = []
def audit(event, args):
    if event in {"open", "os.listdir", "subprocess.Popen", "socket.connect", "exec"}:
        seen.append((event, str(args[0])[:40] if args else ""))

sys.addaudithook(audit)       # note: audit hooks can never be removed

path = os.path.join(tempfile.gettempdir(), "audit_demo.txt")
with open(path, "w") as f:
    f.write("hi")
os.listdir(tempfile.gettempdir())
exec("x = 1")
os.remove(path)
for event, detail in seen[:6]:
    print(f"AUDIT {event:<12} {detail}")
```

### Example 3: sys.excepthook, atexit and sys.monitoring  ([`example_3.py`](example_3.py))

```python
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
```

## Practice

1. Build a call-graph tracer that prints nested calls with indentation.
2. Block `socket.connect` with an audit hook (raise an exception inside the hook) to sandbox a test.
3. Use `sys.setprofile` to measure how long each function takes.

---

[⬅ Day 120](../Day-120-Advanced-Structural-Pattern-Matching/README.md) · [🏠 Home](../README.md) · [Day 122 ➡](../Day-122-Advanced-Concurrency-Patterns/README.md)

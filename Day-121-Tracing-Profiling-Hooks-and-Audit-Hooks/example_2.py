# Day 121 · Tracing, Profiling Hooks and Audit Hooks — Audit hooks: watching what code does
# Run: python example_2.py

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

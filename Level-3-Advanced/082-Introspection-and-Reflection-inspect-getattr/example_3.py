# 082 · Introspection and Reflection (inspect, getattr) — Example 3: The call stack and a command dispatcher
# Run: python example_3.py

import inspect

def who_called_me():
    caller = inspect.stack()[1]
    return f"called from {caller.function}() at line {caller.lineno}"

def report():
    print(who_called_me())

report()

class Shell:
    def do_hello(self, arg): return f"Hello {arg}"
    def do_add(self, arg): return sum(map(int, arg.split()))
    def run(self, line):
        cmd, _, arg = line.partition(" ")
        handler = getattr(self, f"do_{cmd}", None)
        return handler(arg) if handler else f"unknown: {cmd}"

sh = Shell()
for line in ["hello world", "add 1 2 3", "jump"]:
    print(line, "=>", sh.run(line))
commands = [n[3:] for n, _ in inspect.getmembers(sh, inspect.ismethod) if n.startswith("do_")]
print("available commands:", commands)

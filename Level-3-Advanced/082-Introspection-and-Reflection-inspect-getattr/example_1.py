# 082 · Introspection and Reflection (inspect, getattr) — Example 1: dir, vars, getattr and setattr
# Run: python example_1.py

class Robot:
    def __init__(self):
        self.name = "R2"
        self.battery = 80
    def walk(self): return "walking"
    def talk(self): return "beep"

r = Robot()
print([m for m in dir(r) if not m.startswith("_")])
print(vars(r))
for action in ["walk", "talk", "fly"]:
    method = getattr(r, action, None)
    print(action, "->", method() if callable(method) else "not supported")
setattr(r, "battery", 100)
print(r.battery, hasattr(r, "name"))

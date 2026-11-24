# Day 081 · Metaclasses — A metaclass that enforces rules and registers classes
# Run: python example_2.py

class PluginMeta(type):
    registry = {}

    def __new__(mcls, name, bases, ns):
        cls = super().__new__(mcls, name, bases, ns)
        if bases:                                  # skip the base class itself
            if "run" not in ns:
                raise TypeError(f"{name} must define run()")
            mcls.registry[name.lower()] = cls
        return cls

class Plugin(metaclass=PluginMeta):
    pass

class Resize(Plugin):
    def run(self): return "resizing"

class Blur(Plugin):
    def run(self): return "blurring"

print(PluginMeta.registry)
print([cls().run() for cls in PluginMeta.registry.values()])
try:
    class Broken(Plugin):
        pass
except TypeError as e:
    print("TypeError:", e)

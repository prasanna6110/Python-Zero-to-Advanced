# Day 092 · Introspection and Reflection (inspect, getattr) — inspect.signature for automatic validation
# Run: python example_2.py

import inspect

def create_user(name: str, age: int, active: bool = True) -> dict:
    """Create a user record."""
    return {"name": name, "age": age, "active": active}

sig = inspect.signature(create_user)
print(sig)
for p in sig.parameters.values():
    print(f"  {p.name}: {p.annotation.__name__}, default={p.default if p.default is not p.empty else '-'}")

bound = sig.bind("Asha", 21)
bound.apply_defaults()
print(bound.arguments)
print(inspect.getdoc(create_user), "| source lines:", len(inspect.getsource(create_user).splitlines()))

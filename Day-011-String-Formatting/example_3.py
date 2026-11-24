# Day 011 · String Formatting — Debugging with f-strings
# Run: python example_3.py

x, y = 10, 3
print(f"{x=}, {y=}, {x / y=:.3f}")
name = "Python"
print(f"{name!r} has {len(name)} letters, upper: {name.upper()}")
width = 12
print(f"{'center':^{width}}|")    # nested braces for a dynamic width

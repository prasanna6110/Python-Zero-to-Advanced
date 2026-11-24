# Day 126 · Writing Pythonic Code (Idioms and Best Practices) — EAFP vs LBYL
# Run: python example_2.py

config = {"host": "localhost"}

# LBYL
if "port" in config:
    port = config["port"]
else:
    port = 8000

# EAFP
try:
    port = config["port"]
except KeyError:
    port = 8000

# Best: a built-in made for exactly this
port = config.get("port", 8000)
print(port)

def to_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None
print([to_int(v) for v in ["5", "x", None, "42"]])

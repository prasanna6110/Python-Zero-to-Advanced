# 044 · Dataclasses — Example 3: Frozen dataclasses and helpers
# Run: python example_3.py

from dataclasses import dataclass, asdict, astuple, replace

@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float

delhi = Coordinate(28.61, 77.21)
print(asdict(delhi), astuple(delhi))
moved = replace(delhi, lat=29.97)     # creates a new object
print(moved)
print({delhi: "Delhi"})               # frozen makes it hashable
try:
    delhi.lat = 0
except Exception as e:
    print(type(e).__name__, e)

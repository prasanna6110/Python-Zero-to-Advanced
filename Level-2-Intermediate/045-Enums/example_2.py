# 045 · Enums — Example 2: auto, methods and match
# Run: python example_2.py

from enum import Enum, auto

class Planet(Enum):
    MERCURY = auto()
    EARTH = auto()
    MARS = auto()

    def describe(self):
        match self:
            case Planet.EARTH:
                return "home"
            case _:
                return "far away"

for p in Planet:
    print(p.value, p.name, p.describe())

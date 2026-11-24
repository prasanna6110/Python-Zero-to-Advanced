# 106 · Modern Python Features (3.10 to 3.13) — Example 3: The type statement, @override and copy.replace
# Run: python example_3.py

import sys
from typing import override
from dataclasses import dataclass

type Vector = list[float]
type Mapping[K, V] = dict[K, list[V]]

def scale(v: Vector, k: float) -> Vector:
    return [x * k for x in v]

class Base:
    def greet(self) -> str: return "base"

class Child(Base):
    @override                         # type checkers complain if Base has no greet()
    def greet(self) -> str: return "child"

@dataclass(frozen=True)
class Config:
    host: str
    port: int

print(scale([1.0, 2.0], 3), Vector.__value__, Child().greet())
if sys.version_info >= (3, 13):
    import copy
    print(copy.replace(Config("localhost", 80), port=443))
else:
    from dataclasses import replace
    print(replace(Config("localhost", 80), port=443))
print("Running on Python", sys.version.split()[0])

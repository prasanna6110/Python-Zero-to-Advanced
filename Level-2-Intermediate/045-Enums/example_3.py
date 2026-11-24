# 045 · Enums — Example 3: IntEnum, StrEnum and Flag
# Run: python example_3.py

from enum import IntEnum, StrEnum, Flag, auto

class Priority(IntEnum):
    LOW = 1
    HIGH = 3

class Env(StrEnum):
    DEV = auto()
    PROD = auto()

class Perm(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()

print(Priority.HIGH > Priority.LOW, Priority.HIGH + 1)
print(Env.PROD, Env.PROD == "prod")
user = Perm.READ | Perm.WRITE
print(user, Perm.WRITE in user, Perm.EXECUTE in user)

# 072 · __init_subclass__, __class_getitem__ and Class Creation Hooks — Example 2: Enforcing an interface on subclasses
# Run: python example_2.py

class Command:
    required = ("execute", "undo")

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        missing = [m for m in cls.required if not callable(getattr(cls, m, None))]
        if missing:
            raise TypeError(f"{cls.__name__} is missing: {', '.join(missing)}")

class Paste(Command):
    def execute(self): return "pasted"
    def undo(self): return "unpasted"

print(Paste().execute())
try:
    class Cut(Command):
        def execute(self): ...
except TypeError as e:
    print("TypeError:", e)

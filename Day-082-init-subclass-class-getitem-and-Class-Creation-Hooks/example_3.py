# Day 082 · __init_subclass__, __class_getitem__ and Class Creation Hooks — __class_getitem__ and __instancecheck__
# Run: python example_3.py

class TypedList(list):
    def __class_getitem__(cls, item_type):
        class Specialized(cls):
            def append(self, value):
                if not isinstance(value, item_type):
                    raise TypeError(f"expected {item_type.__name__}")
                super().append(value)
        Specialized.__name__ = f"TypedList[{item_type.__name__}]"
        return Specialized

IntList = TypedList[int]
nums = IntList()
nums.append(5)
try:
    nums.append("x")
except TypeError as e:
    print(IntList.__name__, "->", e)

class DuckCheck(type):
    def __instancecheck__(cls, obj):
        return hasattr(obj, "quack")

class Duckish(metaclass=DuckCheck): pass
class Robot:
    def quack(self): ...
print(isinstance(Robot(), Duckish), isinstance(42, Duckish))

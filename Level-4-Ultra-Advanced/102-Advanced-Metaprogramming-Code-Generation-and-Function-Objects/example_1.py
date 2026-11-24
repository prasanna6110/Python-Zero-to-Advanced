# 102 · Advanced Metaprogramming: Code Generation and Function Objects — Example 1: Generating a record class with exec (how namedtuple works)
# Run: python example_1.py

def make_record(name, fields):
    args = ", ".join(fields)
    assigns = "\n".join(f"        self.{f} = {f}" for f in fields) or "        pass"
    reprs = ", ".join(f"{f}={{self.{f}!r}}" for f in fields)
    src = f"""
class {name}:
    __slots__ = {tuple(fields)!r}
    def __init__(self, {args}):
{assigns}
    def __repr__(self):
        return f"{name}({reprs})"
    def __eq__(self, other):
        return all(getattr(self, f) == getattr(other, f) for f in self.__slots__)
"""
    namespace = {}
    exec(src, namespace)
    cls = namespace[name]
    cls._source = src
    return cls

Student = make_record("Student", ["name", "roll", "cgpa"])
s = Student("Asha", 101, 9.1)
print(s, s == Student("Asha", 101, 9.1))
print(Student._source)

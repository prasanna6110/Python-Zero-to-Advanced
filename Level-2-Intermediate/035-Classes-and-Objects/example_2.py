# 035 · Classes and Objects — Example 2: Attributes and methods
# Run: python example_2.py

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def report(self):
        print(f"{self.name}: average {self.average():.1f}")

s = Student("Asha", [90, 85, 77])
s.report()
s.marks.append(100)
s.report()
print(vars(s))         # the object's attributes as a dict

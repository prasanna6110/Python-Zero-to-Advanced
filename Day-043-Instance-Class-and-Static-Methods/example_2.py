# Day 043 · Instance, Class and Static Methods — Class methods as alternative constructors
# Run: python example_2.py

class Date:
    def __init__(self, day, month, year):
        self.day, self.month, self.year = day, month, year

    @classmethod
    def from_string(cls, text):            # "13-01-1998"
        d, m, y = map(int, text.split("-"))
        return cls(d, m, y)

    @staticmethod
    def is_leap(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def __repr__(self):
        return f"Date({self.day}, {self.month}, {self.year})"

d = Date.from_string("13-01-1998")
print(d, Date.is_leap(2024), Date.is_leap(1900))

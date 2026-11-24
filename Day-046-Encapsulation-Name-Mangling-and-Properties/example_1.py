# Day 046 · Encapsulation, Name Mangling and Properties — Protected and private
# Run: python example_1.py

class Account:
    def __init__(self, balance):
        self._bank = "SBI"          # protected (convention)
        self.__pin = 1234           # private (name-mangled)
        self.balance = balance

    def check_pin(self, pin):
        return pin == self.__pin

a = Account(500)
print(a._bank, a.check_pin(1234))
try:
    print(a.__pin)
except AttributeError as e:
    print("AttributeError:", e)
print("Mangled name still exists:", a._Account__pin)

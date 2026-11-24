# 039 · Multiple Inheritance, MRO and super() — Example 2: Diamond and cooperative super()
# Run: python example_2.py

class A:
    def hello(self):
        print("A")

class B(A):
    def hello(self):
        print("B"); super().hello()

class C(A):
    def hello(self):
        print("C"); super().hello()

class D(B, C):
    def hello(self):
        print("D"); super().hello()

D().hello()          # D B C A: each class runs once
print([k.__name__ for k in D.mro()])

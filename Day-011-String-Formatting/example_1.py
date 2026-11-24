# Day 011 · String Formatting — Three ways compared
# Run: python example_1.py

name, marks = "Neha", 92.456
print(f"{name} scored {marks:.2f}")
print("{} scored {:.2f}".format(name, marks))
print("%s scored %.2f" % (name, marks))
print("{n} scored {m:.1f}".format(n=name, m=marks))

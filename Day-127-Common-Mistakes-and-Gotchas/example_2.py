# Day 127 · Common Mistakes and Gotchas — Scope, iterators and type gotchas
# Run: python example_2.py

count = 0
def increment():
    try:
        count += 1                     # UnboundLocalError
    except UnboundLocalError as e:
        print("UnboundLocalError:", e)
increment()

squares = (x * x for x in range(3))
print(list(squares), list(squares), "<- a generator can only be used once")

print('"10" > "9" ->', "10" > "9", "| 10 > 9 ->", 10 > 9)
print("3 / 2 =", 3 / 2, "| 3 // 2 =", 3 // 2, "| -3 // 2 =", -3 // 2)
print("(1) is", type((1)).__name__, "| (1,) is", type((1,)).__name__)
print("0.1 * 3 == 0.3 ->", 0.1 * 3 == 0.3)
print("True + True =", True + True, "(bool is a subclass of int)")

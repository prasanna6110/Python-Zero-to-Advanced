# 048 · Closures — Example 1: A basic closure
# Run: python example_1.py

def outer(message):
    def inner():
        print("Message:", message)
    return inner

say_hi = outer("Hi!")
say_bye = outer("Bye!")
say_hi()
say_bye()
print(say_hi.__closure__[0].cell_contents)

# 016 · Function Arguments in Depth — Example 2: *args and **kwargs
# Run: python example_2.py

def total(*numbers):
    print("args tuple:", numbers)
    return sum(numbers)

def profile(name, **details):
    print("Name:", name)
    for key, value in details.items():
        print(f"  {key}: {value}")

print(total(1, 2, 3, 4))
profile("Kiran", age=22, city="Pune", branch="ECE")

nums = [10, 20, 30]
info = {"age": 30, "city": "Delhi"}
print(total(*nums))
profile("Mohan", **info)

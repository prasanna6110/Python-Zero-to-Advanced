# Day 018 · Functions Basics — Returning multiple values
# Run: python example_2.py

def stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

low, high, avg = stats([4, 8, 15, 16, 23, 42])
print(f"min={low} max={high} avg={avg:.2f}")

def say_hi():
    print("hi")
result = say_hi()
print("Return value of say_hi:", result)   # None

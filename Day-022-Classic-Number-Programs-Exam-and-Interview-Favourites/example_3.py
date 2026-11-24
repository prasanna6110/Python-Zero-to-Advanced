# Day 022 · Classic Number Programs (Exam and Interview Favourites) — Fibonacci, factorial, binary conversion and leap years
# Run: python example_3.py

def fibonacci(n):
    a, b, out = 0, 1, []
    for _ in range(n):
        out.append(a)
        a, b = b, a + b
    return out

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def to_binary(n):
    if n == 0:
        return "0"
    bits = ""
    while n > 0:
        bits = str(n % 2) + bits
        n //= 2
    return bits

def is_leap(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

print("Fibonacci:", fibonacci(15))
print("20! =", factorial(20))
print("25 in binary:", to_binary(25), "| check:", bin(25))
print("Leap years:", [y for y in [1900, 1996, 2000, 2024, 2026] if is_leap(y)])
print("Sum of digits of 98765:", sum(map(int, str(98765))))

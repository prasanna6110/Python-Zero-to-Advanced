# 018 · Recursion — Example 1: Factorial and sum of digits
# Run: python example_1.py

def factorial(n):
    if n <= 1:          # base case
        return 1
    return n * factorial(n - 1)

def digit_sum(n):
    return n if n < 10 else n % 10 + digit_sum(n // 10)

print(factorial(5), factorial(10))
print(digit_sum(98765))

# Day 022 · Classic Number Programs (Exam and Interview Favourites) — Armstrong, perfect, strong and palindrome numbers
# Run: python example_2.py

from math import factorial

def digits(n):
    return [int(d) for d in str(n)]

def is_armstrong(n):
    k = len(str(n))
    return n == sum(d ** k for d in digits(n))

def is_perfect(n):
    return n > 1 and n == sum(d for d in range(1, n // 2 + 1) if n % d == 0)

def is_strong(n):
    return n == sum(factorial(d) for d in digits(n))

def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev

print("Armstrong < 10000:", [n for n in range(1, 10000) if is_armstrong(n)])
print("Perfect < 10000:", [n for n in range(1, 10000) if is_perfect(n)])
print("Strong < 100000:", [n for n in range(1, 100000) if is_strong(n)])
print("Palindromes 100-200:", [n for n in range(100, 200) if n == reverse_number(n)])

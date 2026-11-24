# Day 022 · Classic Number Programs (Exam and Interview Favourites)

_Beginner_

## Programs every Python student should be able to write
| Program | Idea |
|---------|------|
| Prime check | test divisors up to √n |
| Primes up to N | Sieve of Eratosthenes |
| Factorial | loop or recursion |
| Fibonacci | `a, b = b, a + b` |
| GCD / LCM | Euclid: `gcd(a, b) = gcd(b, a % b)`, `lcm = a * b // gcd` |
| Palindrome number | reverse its digits |
| Armstrong number | sum of digits raised to the number of digits equals the number (153) |
| Perfect number | sum of its proper divisors equals the number (6, 28) |
| Strong number | sum of the factorials of its digits equals the number (145) |
| Sum of digits / reverse | `% 10` and `// 10` |
| Decimal → binary | repeatedly divide by 2 |
| Leap year | divisible by 4 and (not by 100, or by 400) |

Learn **both** approaches: the maths way (with `%` and `//`) and the Pythonic way (with `str()` and built-ins).

## Examples

### Example 1: Primes, sieve, GCD and LCM  ([`example_1.py`](example_1.py))

```python
def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

def sieve(limit):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if flags[i]:
            for j in range(i * i, limit + 1, i):
                flags[j] = False
    return [i for i, f in enumerate(flags) if f]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print([n for n in range(30) if is_prime(n)])
print("primes up to 100:", sieve(100))
print("gcd(48, 180) =", gcd(48, 180), "| lcm =", 48 * 180 // gcd(48, 180))
```

### Example 2: Armstrong, perfect, strong and palindrome numbers  ([`example_2.py`](example_2.py))

```python
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
```

### Example 3: Fibonacci, factorial, binary conversion and leap years  ([`example_3.py`](example_3.py))

```python
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
```

## Practice

1. Print all twin primes below 100 (pairs like 11 and 13).
2. Check whether a number is a "happy number".
3. Convert a binary string back to decimal without using `int(x, 2)`.
4. Find the HCF of a list of numbers.

---

[⬅ Day 021](../Day-021-Recursion/README.md) · [🏠 Home](../README.md) · [Day 023 ➡](../Day-023-Classic-String-Programs/README.md)

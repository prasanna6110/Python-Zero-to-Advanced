# Day 022 · Classic Number Programs (Exam and Interview Favourites) — Primes, sieve, GCD and LCM
# Run: python example_1.py

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

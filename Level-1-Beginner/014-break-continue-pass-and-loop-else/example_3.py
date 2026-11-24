# 014 · break, continue, pass and loop-else — Example 3: Loop-else for searching (prime check)
# Run: python example_3.py

for n in [7, 12, 29]:
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            print(f"{n} is not prime (divisible by {d})")
            break
    else:
        print(f"{n} is prime")

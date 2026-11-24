# Day 133 · Project: Password Generator and Strength Checker — Password Generator and Strength Checker
# Run: python main.py

import math
import re
import secrets
import string
import sys

DEMO = not sys.stdin.isatty()
WORDS = ["tiger", "river", "cloud", "mango", "rocket", "pixel", "garden", "silver", "python", "monsoon"]

def generate(length=16, upper=True, digits=True, symbols=True):
    pools = [string.ascii_lowercase]
    if upper: pools.append(string.ascii_uppercase)
    if digits: pools.append(string.digits)
    if symbols: pools.append("!@#$%^&*-_=+?")
    password = [secrets.choice(p) for p in pools]          # at least one from each pool
    alphabet = "".join(pools)
    password += [secrets.choice(alphabet) for _ in range(length - len(password))]
    secrets.SystemRandom().shuffle(password)
    return "".join(password)

def passphrase(n=4):
    return "-".join(secrets.choice(WORDS).capitalize() for _ in range(n)) + str(secrets.randbelow(100))

def strength(pw):
    checks = {
        "at least 12 characters": len(pw) >= 12,
        "lowercase letter": bool(re.search(r"[a-z]", pw)),
        "uppercase letter": bool(re.search(r"[A-Z]", pw)),
        "digit": bool(re.search(r"\d", pw)),
        "symbol": bool(re.search(r"[^A-Za-z0-9]", pw)),
        "no repeated runs like 'aaa'": not re.search(r"(.)\1\1", pw),
        "not a common password": pw.lower() not in {"password", "123456", "qwerty", "admin", "letmein"},
    }
    pool = sum([26 * checks["lowercase letter"], 26 * checks["uppercase letter"],
                10 * checks["digit"], 20 * checks["symbol"]]) or 1
    entropy = len(pw) * math.log2(pool)
    score = sum(checks.values())
    label = ["Very weak", "Very weak", "Weak", "Weak", "Medium", "Strong", "Strong", "Very strong"][score]
    return label, entropy, [k for k, ok in checks.items() if not ok]

def main():
    print("🔐 PASSWORD TOOL")
    print("Generated:", generate(16))
    print("Passphrase:", passphrase())
    tests = ["password", "Hello123", "Tr0ub4dor&3", generate(20)] if DEMO else [input("Password to check: ")]
    for pw in tests:
        label, bits, missing = strength(pw)
        print(f"\n{pw!r}: {label} (~{bits:.0f} bits of entropy)")
        for m in missing:
            print("   ✗ missing:", m)

if __name__ == "__main__":
    main()

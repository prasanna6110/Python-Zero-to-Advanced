# 060 · Regular Expressions (re) — Example 3: Validation with fullmatch and lookahead
# Run: python example_3.py

import re

def strong_password(p):
    return bool(re.fullmatch(r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%!]).{8,}", p))

for pw in ["password", "Passw0rd", "Passw0rd!", "Ab1!"]:
    print(f"{pw:<10} strong={strong_password(pw)}")

def valid_pan(pan):          # Indian PAN format: ABCDE1234F
    return re.fullmatch(r"[A-Z]{5}\d{4}[A-Z]", pan) is not None
print(valid_pan("ABCDE1234F"), valid_pan("abcde1234f"))
print(re.sub(r"(\w+)@(\w+)", r"\2 at \1", "user@domain"))

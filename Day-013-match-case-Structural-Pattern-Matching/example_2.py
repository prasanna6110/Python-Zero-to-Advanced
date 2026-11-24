# Day 013 · match-case (Structural Pattern Matching) — Guards and capture
# Run: python example_2.py

def classify(n):
    match n:
        case 0:
            return "zero"
        case x if x < 0:
            return f"negative ({x})"
        case x if x % 2 == 0:
            return f"positive even ({x})"
        case x:
            return f"positive odd ({x})"

for n in [0, -3, 8, 7]:
    print(classify(n))

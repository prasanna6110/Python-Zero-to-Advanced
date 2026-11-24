# Day 013 · match-case (Structural Pattern Matching) — Basic match
# Run: python example_1.py

def http_status(code):
    match code:
        case 200:
            return "OK"
        case 301 | 302:
            return "Redirect"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown"

for c in [200, 302, 404, 999]:
    print(c, "->", http_status(c))

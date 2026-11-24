# Day 033 · Exception Handling: try, except, else, finally — Retrying with a safe input function
# Run: python example_3.py

def safe_int(values):
    """Try each value until one is a valid int (simulates repeated input)."""
    for attempt, v in enumerate(values, 1):
        try:
            return int(v)
        except ValueError:
            print(f"Attempt {attempt}: {v!r} is invalid, try again")
    return None

print("Got:", safe_int(["ten", "1O", "10"]))

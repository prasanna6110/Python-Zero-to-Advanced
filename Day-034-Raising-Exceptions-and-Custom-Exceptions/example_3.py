# Day 034 · Raising Exceptions and Custom Exceptions — Re-raising and chaining
# Run: python example_3.py

def load_config(text):
    try:
        key, value = text.split("=")
    except ValueError as e:
        raise RuntimeError(f"bad config line: {text!r}") from e
    return {key: value}

try:
    load_config("no-equals-sign")
except RuntimeError as e:
    print("Error:", e)
    print("Caused by:", repr(e.__cause__))

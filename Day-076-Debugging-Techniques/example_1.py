# Day 076 · Debugging Techniques — Reading and formatting tracebacks
# Run: python example_1.py

import traceback

def level3(data):
    return data["missing"]

def level2(data):
    return level3(data)

def level1():
    return level2({"a": 1})

try:
    level1()
except KeyError:
    print("Traceback (read from the bottom up):")
    print(traceback.format_exc())

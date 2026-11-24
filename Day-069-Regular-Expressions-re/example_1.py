# Day 069 · Regular Expressions (re) — search, findall, sub
# Run: python example_1.py

import re

text = "Call 98765-43210 or 91234-56789. Email: prasanna@nitkkr.ac.in, help@site.com"
print(re.findall(r"\d{5}-\d{5}", text))
print(re.findall(r"[\w.]+@[\w.]+\.\w+", text))
m = re.search(r"(\d{5})-(\d{5})", text)
print(m.group(), m.group(1), m.span())
print(re.sub(r"\d{5}-\d{5}", "XXXXX-XXXXX", text))
print(re.split(r"[,.\s]+", "a, b. c  d"))

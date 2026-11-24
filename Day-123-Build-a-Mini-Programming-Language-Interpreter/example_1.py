# Day 123 · Build a Mini Programming Language (Interpreter) — Step 1: the lexer
# Run: python example_1.py

import re

TOKEN_SPEC = [
    ("NUM", r"\d+(\.\d+)?"),
    ("ID", r"[A-Za-z_]\w*"),
    ("OP", r"[+\-*/()=]"),
    ("NEWLINE", r"\n"),
    ("SKIP", r"[ \t]+"),
    ("ERROR", r"."),
]
MASTER = re.compile("|".join(f"(?P<{name}>{pat})" for name, pat in TOKEN_SPEC))
KEYWORDS = {"let", "print"}

def tokenize(code):
    for m in MASTER.finditer(code):
        kind, value = m.lastgroup, m.group()
        if kind == "SKIP":
            continue
        if kind == "ERROR":
            raise SyntaxError(f"unexpected character {value!r}")
        if kind == "ID" and value in KEYWORDS:
            kind = value.upper()
        if kind == "NUM":
            value = float(value)
        yield (kind, value)

for tok in tokenize("let x = 2 * (3 + 4)\nprint x"):
    print(tok)

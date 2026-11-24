# Day 123 · Build a Mini Programming Language (Interpreter) — Step 2 and 3: parser and evaluator
# Run: python example_2.py

import re

MASTER = re.compile(r"(?P<NUM>\d+(?:\.\d+)?)|(?P<ID>[A-Za-z_]\w*)|(?P<OP>[+\-*/()=])|(?P<NL>\n)|(?P<WS>[ \t]+)")
def tokenize(code):
    toks = []
    for m in MASTER.finditer(code):
        k, v = m.lastgroup, m.group()
        if k == "WS": continue
        if k == "ID" and v in ("let", "print"): k = v.upper()
        toks.append((k, float(v) if k == "NUM" else v))
    return toks + [("EOF", None)]

class Parser:
    def __init__(self, tokens): self.toks, self.i = tokens, 0
    def peek(self): return self.toks[self.i]
    def eat(self, kind=None, value=None):
        k, v = self.toks[self.i]
        if (kind and k != kind) or (value and v != value):
            raise SyntaxError(f"expected {value or kind}, got {v!r}")
        self.i += 1
        return v
    def program(self):
        stmts = []
        while self.peek()[0] != "EOF":
            if self.peek()[0] == "NL": self.eat(); continue
            stmts.append(self.statement())
        return stmts
    def statement(self):
        if self.peek()[0] == "LET":
            self.eat(); name = self.eat("ID"); self.eat("OP", "=")
            return ("let", name, self.expr())
        if self.peek()[0] == "PRINT":
            self.eat(); return ("print", self.expr())
        raise SyntaxError(f"unknown statement {self.peek()}")
    def expr(self):
        node = self.term()
        while self.peek() in (("OP", "+"), ("OP", "-")):
            node = ("bin", self.eat(), node, self.term())
        return node
    def term(self):
        node = self.factor()
        while self.peek() in (("OP", "*"), ("OP", "/")):
            node = ("bin", self.eat(), node, self.factor())
        return node
    def factor(self):
        k, v = self.peek()
        if k == "NUM": self.eat(); return ("num", v)
        if k == "ID": self.eat(); return ("var", v)
        if (k, v) == ("OP", "-"): self.eat(); return ("neg", self.factor())
        if (k, v) == ("OP", "("):
            self.eat(); node = self.expr(); self.eat("OP", ")"); return node
        raise SyntaxError(f"unexpected {v!r}")

def evaluate(node, env):
    match node:
        case ("num", v): return v
        case ("var", name):
            if name not in env: raise NameError(f"undefined variable {name!r}")
            return env[name]
        case ("neg", x): return -evaluate(x, env)
        case ("bin", op, l, r):
            a, b = evaluate(l, env), evaluate(r, env)
            return {"+": a + b, "-": a - b, "*": a * b}[op] if op != "/" else a / b

def run(code):
    env = {}
    for stmt in Parser(tokenize(code)).program():
        match stmt:
            case ("let", name, e): env[name] = evaluate(e, env)
            case ("print", e): print(evaluate(e, env))
    return env

program = """
let radius = 7
let pi = 3.14159
let area = pi * radius * radius
print area
print (2 + 3) * -4
print area / (radius + 3)
"""
run(program)

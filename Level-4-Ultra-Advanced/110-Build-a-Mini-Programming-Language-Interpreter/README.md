# 110 · Build a Mini Programming Language (Interpreter)

## How interpreters work
1. **Lexer (tokenizer)**: turns text into tokens. `"x = 2 + 3"` becomes `[ID x, '=', NUM 2, '+', NUM 3]`.
2. **Parser**: turns tokens into an **AST**, using grammar rules. A **recursive-descent** parser has one function per rule.
3. **Evaluator**: walks the AST and computes results, keeping variables in an **environment**.

## Grammar for our language ("PK-lang")
```
program    := statement*
statement  := "let" ID "=" expr | "print" expr
expr       := term (("+" | "-") term)*
term       := factor (("*" | "/") factor)*
factor     := NUM | ID | "(" expr ")" | "-" factor
```
Operator precedence comes **from the grammar itself**: `term` binds tighter than `expr`.

This is the same pipeline CPython follows, just much smaller.

## Examples

### Example 1: Step 1: the lexer  ([`example_1.py`](example_1.py))

```python
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
```

### Example 2: Step 2 and 3: parser and evaluator  ([`example_2.py`](example_2.py))

```python
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
```

### Example 3: Compiling our language to Python bytecode via the ast module  ([`example_3.py`](example_3.py))

```python
import ast

def compile_to_python(statements):
    """Translate PK-lang tuples into a Python AST, then run real bytecode."""
    def expr(node):
        match node:
            case ("num", v): return ast.Constant(v)
            case ("var", n): return ast.Name(n, ast.Load())
            case ("neg", x): return ast.UnaryOp(ast.USub(), expr(x))
            case ("bin", op, l, r):
                ops = {"+": ast.Add(), "-": ast.Sub(), "*": ast.Mult(), "/": ast.Div()}
                return ast.BinOp(expr(l), ops[op], expr(r))
    body = []
    for s in statements:
        match s:
            case ("let", name, e):
                body.append(ast.Assign([ast.Name(name, ast.Store())], expr(e)))
            case ("print", e):
                body.append(ast.Expr(ast.Call(ast.Name("print", ast.Load()), [expr(e)], [])))
    module = ast.fix_missing_locations(ast.Module(body, type_ignores=[]))
    return module

statements = [
    ("let", "a", ("num", 10.0)),
    ("let", "b", ("bin", "*", ("var", "a"), ("num", 4.0))),
    ("print", ("bin", "+", ("var", "b"), ("neg", ("num", 2.0)))),
]
tree = compile_to_python(statements)
print("Generated Python:\n" + ast.unparse(tree))
print("Output:")
exec(compile(tree, "<pk-lang>", "exec"), {})
```

## Practice

1. Add `if`/`else` and comparison operators to PK-lang.
2. Add functions: `def square(x) = x * x`.
3. Add helpful error messages that include line numbers.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

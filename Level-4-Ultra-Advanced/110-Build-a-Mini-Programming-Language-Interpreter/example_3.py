# 110 · Build a Mini Programming Language (Interpreter) — Example 3: Compiling our language to Python bytecode via the ast module
# Run: python example_3.py

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

# 101 · AST: Parsing, Analysing and Transforming Code — Example 2: A mini linter with NodeVisitor
# Run: python example_2.py

import ast

code = '''
import os, sys
def process(data, verbose=[]):
    try:
        result = eval(data)
    except:
        pass
    print(result)
def helper(): return 1
'''

class Linter(ast.NodeVisitor):
    def __init__(self): self.issues = []
    def visit_FunctionDef(self, node):
        if not ast.get_docstring(node):
            self.issues.append((node.lineno, f"function '{node.name}' has no docstring"))
        for d in node.args.defaults:
            if isinstance(d, (ast.List, ast.Dict, ast.Set)):
                self.issues.append((node.lineno, f"mutable default argument in '{node.name}'"))
        self.generic_visit(node)
    def visit_ExceptHandler(self, node):
        if node.type is None:
            self.issues.append((node.lineno, "bare 'except:'"))
        self.generic_visit(node)
    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id in {"eval", "exec"}:
            self.issues.append((node.lineno, f"dangerous call to {node.func.id}()"))
        self.generic_visit(node)

linter = Linter()
linter.visit(ast.parse(code))
for line, msg in sorted(linter.issues):
    print(f"line {line}: {msg}")

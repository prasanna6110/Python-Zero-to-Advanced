# Day 114 · AST: Parsing, Analysing and Transforming Code

_Ultra Advanced_

## The Abstract Syntax Tree
Python source code is parsed into a tree of nodes, for example `Module → FunctionDef → Return → BinOp`.

```python
import ast
tree = ast.parse(source)
print(ast.dump(tree, indent=2))
```
## Working with the tree
| Tool | Use |
|------|-----|
| `ast.NodeVisitor` | walk the tree and **analyse** it (linters, metrics) |
| `ast.NodeTransformer` | **change** the tree (optimisers, instrumentation) |
| `ast.walk(tree)` | iterate over every node |
| `ast.unparse(tree)` | turn the tree back into source code (3.9+) |
| `compile(tree, ...)` | run a modified tree |
| `ast.literal_eval(s)` | **safely** evaluate literals (a safe replacement for `eval`) |

Tools like pytest's assert rewriting, black, ruff, mypy and many code generators are built on this.

## Examples

### Example 1: Inspecting the tree  ([`example_1.py`](example_1.py))

```python
import ast

source = "def area(r):\n    return 3.14 * r ** 2\n"
tree = ast.parse(source)
print(ast.dump(tree.body[0].body[0], indent=2))
print("\nnode types:", sorted({type(n).__name__ for n in ast.walk(tree)}))
print(ast.literal_eval("{'a': [1, 2, (3, 4)], 'b': True}"))
try:
    ast.literal_eval("__import__('os').system('echo hacked')")
except ValueError as e:
    print("literal_eval refused unsafe code:", type(e).__name__)
```

### Example 2: A mini linter with NodeVisitor  ([`example_2.py`](example_2.py))

```python
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
```

### Example 3: Transforming code with NodeTransformer  ([`example_3.py`](example_3.py))

```python
import ast

class ConstantFolder(ast.NodeTransformer):
    """Replace constant expressions like 60 * 60 * 24 with their value."""
    def visit_BinOp(self, node):
        self.generic_visit(node)
        if isinstance(node.left, ast.Constant) and isinstance(node.right, ast.Constant):
            try:
                value = eval(compile(ast.Expression(node), "<fold>", "eval"))
                return ast.copy_location(ast.Constant(value), node)
            except Exception:
                return node
        return node

class AddPrintTracing(ast.NodeTransformer):
    """Insert a print at the start of every function."""
    def visit_FunctionDef(self, node):
        trace = ast.parse(f"print('-> entering {node.name}')").body[0]
        node.body.insert(0, trace)
        return node

src = "SECONDS_PER_DAY = 60 * 60 * 24\ndef greet(n):\n    return 'Hi ' + n * 2\nprint(greet('ha'), SECONDS_PER_DAY)"
tree = ast.parse(src)
tree = AddPrintTracing().visit(ConstantFolder().visit(tree))
ast.fix_missing_locations(tree)
print("Transformed source:\n" + ast.unparse(tree))
print("\nRunning it:")
exec(compile(tree, "<transformed>", "exec"), {})
```

## Practice

1. Count the functions, classes and imports in any `.py` file.
2. Write a transformer that renames a variable everywhere.
3. Build a safe calculator that only allows numbers and `+ - * /` nodes.

---

[⬅ Day 113](../Day-113-The-Import-System-importlib-and-Import-Hooks/README.md) · [🏠 Home](../README.md) · [Day 115 ➡](../Day-115-Advanced-Metaprogramming-Code-Generation-and-Function-Objects/README.md)

# 101 · AST: Parsing, Analysing and Transforming Code — Example 3: Transforming code with NodeTransformer
# Run: python example_3.py

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

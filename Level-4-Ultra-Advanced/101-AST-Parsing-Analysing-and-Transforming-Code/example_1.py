# 101 · AST: Parsing, Analysing and Transforming Code — Example 1: Inspecting the tree
# Run: python example_1.py

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

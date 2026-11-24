# Day 091 · Python Internals: Bytecode and dis — compile() and code objects
# Run: python example_2.py

src = "x = 10\ny = x * 3\nresult = x + y"
code = compile(src, "<my_program>", "exec")
print(type(code), code.co_names)
namespace = {}
exec(code, namespace)
print("result =", namespace["result"])

expr = compile("2 ** 10 + 1", "<expr>", "eval")
print(eval(expr))

# 081 · Python Internals: Bytecode and dis

## How Python runs your code
`source (.py)` → **tokenize** → **parse** (AST) → **compile** to **bytecode** → the **interpreter** (the PVM, a stack machine) executes it.

- Bytecode is cached in `__pycache__/*.pyc` files.
- `dis.dis(func)` shows the bytecode instructions.
- `func.__code__` is the **code object**, with `co_varnames`, `co_consts`, `co_names`, `co_code`...
- `compile(src, filename, mode)` returns a code object (mode is `"exec"`, `"eval"` or `"single"`).

## Why care?
- To understand performance (local variables are faster than global lookups, for example).
- To see what syntax "really does".
- The **specializing adaptive interpreter** (3.11+) speeds up hot code automatically.

## Examples

### Example 1: Disassembling a function  ([`example_1.py`](example_1.py))

```python
import dis

def add(a, b):
    c = a + b
    return c * 2

dis.dis(add)
code = add.__code__
print("varnames:", code.co_varnames, "| consts:", code.co_consts, "| argcount:", code.co_argcount)
```

### Example 2: compile() and code objects  ([`example_2.py`](example_2.py))

```python
src = "x = 10\ny = x * 3\nresult = x + y"
code = compile(src, "<my_program>", "exec")
print(type(code), code.co_names)
namespace = {}
exec(code, namespace)
print("result =", namespace["result"])

expr = compile("2 ** 10 + 1", "<expr>", "eval")
print(eval(expr))
```

### Example 3: Why local variables are faster  ([`example_3.py`](example_3.py))

```python
import dis, timeit, math

def use_global(n):
    return [math.sqrt(i) for i in range(n)]

def use_local(n):
    sqrt = math.sqrt                    # look up once, keep it in a local
    return [sqrt(i) for i in range(n)]

print("global:", timeit.timeit(lambda: use_global(10_000), number=200))
print("local :", timeit.timeit(lambda: use_local(10_000), number=200))
ops = {ins.opname for ins in dis.get_instructions(use_global)}
print("some opcodes used:", sorted(ops)[:8])
```

## Practice

1. Compare `dis` output for `x = [i for i in range(3)]` and for a for-loop version.
2. Find where your `.pyc` files are stored.
3. Use `compile()` with `"single"` mode and see what happens.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

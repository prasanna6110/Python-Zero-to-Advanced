# Day 003 · Keywords, Identifiers, Indentation and Code Structure

_Beginner_

## Keywords
Keywords are **reserved words** with a special meaning, so you can't use them as variable names. Python has 35 of them:
`False None True and as assert async await break class continue def del elif else except finally for from global if import in is lambda nonlocal not or pass raise return try while with yield`

There are also **soft keywords** (`match`, `case`, `type`, `_`) that are only special in certain places.

## Identifiers
An identifier is the name of a variable, function or class. Remember:
- It may contain letters, digits and `_`, but can't start with a digit.
- It is case-sensitive: `age`, `Age` and `AGE` are three different names.
- `_single` means internal use, `__double` triggers name mangling, and `__dunder__` is a special method.

## Indentation
Python uses **indentation** (4 spaces) to mark blocks, where other languages use `{ }`. Mixing tabs and spaces causes `TabError`. A missing indent gives `IndentationError`.

## Statements and lines
- One statement per line is normal. You can write `a = 1; b = 2`, but it's discouraged.
- A long line can continue inside brackets `( )`, `[ ]` or `{ }`, or after a backslash `\`.
- Python runs a file **from top to bottom**.

## Common beginner errors
| Error | Usual cause |
|-------|-------------|
| `SyntaxError` | a missing `:` or quote, or an unclosed bracket |
| `IndentationError` | wrong spaces at the start of a line |
| `NameError` | a typo, or a variable used before it's created |
| `TypeError` | mixing types, like `"5" + 5` |

## Examples

### Example 1: All keywords and checking names  ([`example_1.py`](example_1.py))

```python
import keyword

print("Number of keywords:", len(keyword.kwlist))
print(keyword.kwlist)
print("Soft keywords:", keyword.softkwlist)
for name in ["for", "total", "class", "my_var", "2cool", "match"]:
    print(f"{name!r:10} keyword={keyword.iskeyword(name)!s:5} valid identifier={name.isidentifier()}")
```

### Example 2: Indentation defines blocks  ([`example_2.py`](example_2.py))

```python
marks = 72
if marks >= 40:
    print("Passed")          # inside the if block (4 spaces)
    if marks >= 70:
        print("Distinction")  # nested block (8 spaces)
print("This line always runs")   # back at the top level

total = (10 + 20 +
         30 + 40)            # a line can continue inside brackets
items = [
    "pen",
    "book",
]
print(total, items)
```

### Example 3: Seeing errors on purpose (and reading them)  ([`example_3.py`](example_3.py))

```python
samples = {
    "SyntaxError": "if True print('hi')",
    "IndentationError": "if True:\nprint('hi')",
    "NameError": "print(totl)",
    "TypeError": "print('5' + 5)",
}
for expected, code in samples.items():
    try:
        exec(code)
    except Exception as e:
        print(f"{expected:<17} -> {type(e).__name__}: {e}")
```

## Practice

1. Try to make a variable named `class`. What error do you get?
2. Write a program with 3 levels of nested `if` blocks.
3. Put an error in your code on purpose, then read the message and fix it.

---

[⬅ Day 002](../Day-002-print-Comments-and-Escape-Sequences/README.md) · [🏠 Home](../README.md) · [Day 004 ➡](../Day-004-Variables-and-Data-Types/README.md)

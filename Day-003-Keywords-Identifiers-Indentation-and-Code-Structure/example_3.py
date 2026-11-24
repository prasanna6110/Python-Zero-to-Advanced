# Day 003 · Keywords, Identifiers, Indentation and Code Structure — Seeing errors on purpose (and reading them)
# Run: python example_3.py

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

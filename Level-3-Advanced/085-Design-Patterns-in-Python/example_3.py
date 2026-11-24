# 085 · Design Patterns in Python — Example 3: Command with undo, Builder and Adapter
# Run: python example_3.py

class TextEditor:
    def __init__(self): self.text, self.history = "", []
    def execute(self, cmd): cmd.do(self); self.history.append(cmd)
    def undo(self): self.history.pop().undo(self)

class Append:
    def __init__(self, s): self.s = s
    def do(self, ed): ed.text += self.s
    def undo(self, ed): ed.text = ed.text[: -len(self.s)]

ed = TextEditor()
for word in ["Hello", " World", "!!!"]:
    ed.execute(Append(word))
print(ed.text); ed.undo(); print("after undo:", ed.text)

class QueryBuilder:
    def __init__(self, table): self.parts = [f"SELECT * FROM {table}"]
    def where(self, cond): self.parts.append(f"WHERE {cond}"); return self
    def order(self, col): self.parts.append(f"ORDER BY {col}"); return self
    def build(self): return " ".join(self.parts)
print(QueryBuilder("users").where("age > 18").order("name").build())

class OldPrinter:
    def print_text(self, t): return f"[old] {t}"
class PrinterAdapter:                      # adapts the old API to a new .write()
    def __init__(self, old): self.old = old
    def write(self, t): return self.old.print_text(t)
print(PrinterAdapter(OldPrinter()).write("adapted!"))

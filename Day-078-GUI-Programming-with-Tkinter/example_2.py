# Day 078 · GUI Programming with Tkinter — A GUI calculator using grid
# Run: python example_2.py

import sys

try:
    import tkinter as tk
    root = tk.Tk()
except Exception as e:
    print("Tkinter window can't open here:", type(e).__name__)
    sys.exit(0)

root.title("Calculator")
display = tk.Entry(root, font=("Consolas", 20), justify="right")
display.grid(row=0, column=0, columnspan=4, sticky="nsew")

def press(key):
    if key == "=":
        try:
            expr = display.get()
            if not all(c in "0123456789+-*/.() " for c in expr):
                raise ValueError
            result = eval(expr, {"__builtins__": {}})   # safe: only digits and operators are allowed
            display.delete(0, tk.END); display.insert(0, str(result))
        except Exception:
            display.delete(0, tk.END); display.insert(0, "Error")
    elif key == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, key)

keys = ["7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "C", "0", "=", "+"]
for i, k in enumerate(keys):
    tk.Button(root, text=k, width=5, height=2, font=("Arial", 14),
              command=lambda k=k: press(k)).grid(row=1 + i // 4, column=i % 4)
if not sys.stdin.isatty():
    root.after(1000, root.destroy)
root.mainloop()

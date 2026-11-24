# Day 078 · GUI Programming with Tkinter

_Intermediate_

## Tkinter: Python's built-in GUI toolkit
```python
import tkinter as tk
root = tk.Tk()
tk.Label(root, text="Hello").pack()
root.mainloop()
```
## Widgets
`Label, Button, Entry, Text, Checkbutton, Radiobutton, Listbox, Scale, Canvas, Frame`, plus `ttk` for modern-looking widgets and `messagebox` and `filedialog` for dialogs.

## Layout managers
Use only one per container:
- `pack()` stacks widgets one after another.
- `grid(row=, column=)` arranges widgets in a table.
- `place(x=, y=)` puts widgets at exact positions.

## Events
- `command=func` on buttons.
- `widget.bind("<Return>", handler)` for keys and mouse events.
- `root.after(ms, func)` for timers and animation.
- `StringVar` / `IntVar` link a variable to a widget.

> These examples open a window. They close automatically only when you run them without a terminal (for example, in automated tests). If there's no display or Tkinter isn't installed, they print a message instead. On Linux, install Tkinter with `sudo apt install python3-tk`.

## Examples

### Example 1: Hello window with a button and an entry box  ([`example_1.py`](example_1.py))

```python
import sys

try:
    import tkinter as tk
    root = tk.Tk()
except Exception as e:
    print("Tkinter window can't open here:", type(e).__name__, "- run this on your own computer.")
    sys.exit(0)

root.title("Day: Tkinter Basics")
root.geometry("320x160")
tk.Label(root, text="Enter your name:", font=("Arial", 12)).pack(pady=5)
name = tk.StringVar()
tk.Entry(root, textvariable=name).pack()
message = tk.Label(root, text="", fg="blue")
message.pack(pady=5)

def greet():
    message.config(text=f"Hello, {name.get() or 'stranger'}! 👋")

tk.Button(root, text="Greet", command=greet).pack()
if not sys.stdin.isatty():
    root.after(1000, root.destroy)
root.mainloop()
```

### Example 2: A GUI calculator using grid  ([`example_2.py`](example_2.py))

```python
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
```

### Example 3: Canvas animation and a to-do list  ([`example_3.py`](example_3.py))

```python
import sys

try:
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
except Exception as e:
    print("Tkinter window can't open here:", type(e).__name__)
    sys.exit(0)

root.title("Canvas + To-Do")
canvas = tk.Canvas(root, width=300, height=120, bg="white")
canvas.pack()
ball = canvas.create_oval(10, 50, 40, 80, fill="orange")
dx = 4

def animate():
    global dx
    x1, _, x2, _ = canvas.coords(ball)
    if x2 >= 300 or x1 <= 0:
        dx = -dx
    canvas.move(ball, dx, 0)
    root.after(20, animate)

entry = tk.Entry(root); entry.pack(fill="x")
tasks = tk.Listbox(root, height=4); tasks.pack(fill="x")
def add_task(event=None):
    if entry.get().strip():
        tasks.insert(tk.END, "• " + entry.get()); entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty", "Type a task first")
entry.bind("<Return>", add_task)
tk.Button(root, text="Add task", command=add_task).pack()
animate()
if not sys.stdin.isatty():
    root.after(1000, root.destroy)
root.mainloop()
```

## Practice

1. Build a BMI calculator GUI.
2. Build a stopwatch GUI with Start, Stop and Reset buttons, using `after()`.
3. Add "Delete selected" and "Save to file" buttons to the to-do list.

---

[⬅ Day 077](../Day-077-Bytes-Encoding-and-Unicode/README.md) · [🏠 Home](../README.md) · [Day 079 ➡](../Day-079-new-vs-init-and-slots/README.md)

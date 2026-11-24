# Day 078 · GUI Programming with Tkinter — Canvas animation and a to-do list
# Run: python example_3.py

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

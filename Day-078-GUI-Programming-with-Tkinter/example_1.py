# Day 078 · GUI Programming with Tkinter — Hello window with a button and an entry box
# Run: python example_1.py

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

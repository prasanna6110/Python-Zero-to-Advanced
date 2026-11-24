# Day 137 · Project: To-Do List Manager (JSON Storage) — To-Do Manager
# Run: python main.py

import json
import sys
from dataclasses import dataclass, asdict, field
from datetime import date
from pathlib import Path

DEMO = not sys.stdin.isatty()
FILE = Path("todo_demo.json" if DEMO else "todo.json")
DEMO_INPUTS = iter(["1", "Finish Micro-Grids assignment", "1", "2026-11-28",
                    "1", "Push course to GitHub", "2", "2026-11-25",
                    "1", "Gym", "3", "", "2", "3", "1", "2", "5", "python", "4", "3", "2", "0"])

def ask(prompt):
    if DEMO:
        v = next(DEMO_INPUTS); print(prompt + v); return v
    return input(prompt)

@dataclass
class Task:
    title: str
    priority: int = 2
    due: str = ""
    done: bool = False
    created: str = field(default_factory=lambda: str(date.today()))

class TodoList:
    def __init__(self, path):
        self.path = path
        self.tasks = [Task(**t) for t in json.loads(path.read_text())] if path.exists() else []
    def save(self):
        self.path.write_text(json.dumps([asdict(t) for t in self.tasks], indent=2))
    def add(self, title, priority, due):
        self.tasks.append(Task(title, priority, due)); self.save()
    def complete(self, i):
        self.tasks[i].done = True; self.save()
    def delete(self, i):
        return self.tasks.pop(i)
    def show(self, items=None):
        items = items if items is not None else list(enumerate(self.tasks))
        if not items:
            print("  (no tasks)"); return
        stars = {1: "🔴 high", 2: "🟡 med ", 3: "🟢 low "}
        for i, t in sorted(items, key=lambda x: (x[1].done, x[1].priority, x[1].due or "9999")):
            print(f"  {i + 1}. [{'✔' if t.done else ' '}] {stars[t.priority]} {t.title:<32} {('due ' + t.due) if t.due else ''}")

def main():
    todo = TodoList(FILE)
    menu = "\n1.Add 2.List 3.Complete 4.Delete 5.Search 0.Exit"
    while True:
        print(menu)
        c = ask("> ")
        if c == "1":
            title = ask("Title: ")
            pr = ask("Priority 1-high 2-med 3-low: ")
            todo.add(title, int(pr) if pr in "123" and pr else 2, ask("Due (YYYY-MM-DD, optional): "))
        elif c == "2":
            todo.show()
        elif c in ("3", "4"):
            todo.show()
            try:
                i = int(ask("Task number: ")) - 1
                if c == "3":
                    todo.complete(i)
                else:
                    print("Deleted:", todo.delete(i).title); todo.save()
            except (ValueError, IndexError):
                print("Invalid number")
        elif c == "5":
            q = ask("Search: ").lower()
            todo.show([(i, t) for i, t in enumerate(todo.tasks) if q in t.title.lower()])
        elif c == "0":
            print("Saved to", FILE); break
    if DEMO:
        FILE.unlink(missing_ok=True)

if __name__ == "__main__":
    main()

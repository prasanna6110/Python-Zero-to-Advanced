# 058 · sys and argparse: Command-Line Programs

## sys
| Attribute | Use |
|-----------|-----|
| `sys.argv` | list of command-line arguments (`argv[0]` is the script name) |
| `sys.exit(code)` | exit the program (0 means success) |
| `sys.path` | where Python searches for modules |
| `sys.stdin / stdout / stderr` | the standard streams |
| `sys.version`, `sys.platform` | information about the interpreter |
| `sys.getsizeof(obj)` | memory size of an object |
| `sys.getrecursionlimit()` | the recursion limit |

## argparse
A proper command-line interface with `--help`, types, defaults and checks.
```python
parser = argparse.ArgumentParser(description="...")
parser.add_argument("filename")                     # positional
parser.add_argument("-n", "--count", type=int, default=1)
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()
```

## Examples

### Example 1: sys basics  ([`example_1.py`](example_1.py))

```python
import sys

print("Script:", sys.argv[0])
print("Arguments:", sys.argv[1:])
print("Platform:", sys.platform, "| Python", sys.version_info[:3])
print("Size of int:", sys.getsizeof(1), "| size of list:", sys.getsizeof([1, 2, 3]))
sys.stderr.write("This goes to stderr\n")
```

### Example 2: argparse CLI  ([`example_2.py`](example_2.py))

```python
import argparse

parser = argparse.ArgumentParser(description="Greeting tool")
parser.add_argument("name", help="who to greet")
parser.add_argument("-n", "--times", type=int, default=1, help="repeat count")
parser.add_argument("--shout", action="store_true", help="uppercase output")
parser.add_argument("--lang", choices=["en", "hi"], default="en")

# Normally: args = parser.parse_args()  e.g.  python example_2.py Ravi -n 2 --shout
args = parser.parse_args(["Ravi", "-n", "2", "--shout", "--lang", "hi"])
word = "Namaste" if args.lang == "hi" else "Hello"
for _ in range(args.times):
    msg = f"{word}, {args.name}!"
    print(msg.upper() if args.shout else msg)
parser.print_help()
```

### Example 3: Subcommands (like git add / git commit)  ([`example_3.py`](example_3.py))

```python
import argparse

parser = argparse.ArgumentParser(prog="todo")
sub = parser.add_subparsers(dest="command", required=True)
add = sub.add_parser("add", help="add a task")
add.add_argument("task")
add.add_argument("--priority", type=int, default=1)
sub.add_parser("list", help="list tasks")

tasks = []
for argv in (["add", "Learn Python", "--priority", "3"], ["add", "Gym"], ["list"]):
    args = parser.parse_args(argv)
    if args.command == "add":
        tasks.append((args.priority, args.task))
        print("Added:", args.task)
    elif args.command == "list":
        for p, t in sorted(tasks, reverse=True):
            print(f"[{p}] {t}")
```

## Practice

1. Write `wordcount.py file.txt --lines --words`.
2. Write a CLI calculator: `calc.py add 2 3`.
3. Exit with code 1 and print a message to stderr if a file is missing.

---

[⬅ Level index](../README.md) · [🏠 Course home](../../README.md)

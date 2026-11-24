# Day 067 · sys and argparse: Command-Line Programs — Subcommands (like git add / git commit)
# Run: python example_3.py

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

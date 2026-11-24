# Day 067 · sys and argparse: Command-Line Programs — argparse CLI
# Run: python example_2.py

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

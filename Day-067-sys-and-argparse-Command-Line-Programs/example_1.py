# Day 067 · sys and argparse: Command-Line Programs — sys basics
# Run: python example_1.py

import sys

print("Script:", sys.argv[0])
print("Arguments:", sys.argv[1:])
print("Platform:", sys.platform, "| Python", sys.version_info[:3])
print("Size of int:", sys.getsizeof(1), "| size of list:", sys.getsizeof([1, 2, 3]))
sys.stderr.write("This goes to stderr\n")

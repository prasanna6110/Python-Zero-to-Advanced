# 029 · File Handling — Example 2: Processing a file line by line
# Run: python example_2.py

import os
path = "marks.txt"
with open(path, "w") as f:
    f.writelines(["Asha,91\n", "Ravi,78\n", "Meera,85\n"])

total = count = 0
with open(path) as f:
    for line in f:
        name, mark = line.strip().split(",")
        total += int(mark)
        count += 1
        print(f"{name:<6} {mark}")
print("Average:", total / count)
os.remove(path)

# 008 · String Methods — Example 3: split, join and validation
# Run: python example_3.py

csv_line = "Ravi,21,CSE,8.9"
parts = csv_line.split(",")
print(parts)
print(" | ".join(parts))

for value in ["12345", "abc", "abc123", "   "]:
    print(f"{value!r}: digit={value.isdigit()} alpha={value.isalpha()} alnum={value.isalnum()}")

print("7".zfill(3), "Title".center(20, "*"))

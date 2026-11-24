# 030 · Modules, Imports and __name__ — Example 3: The __name__ guard
# Run: python example_3.py

def main():
    print("Running main program")

print("__name__ is:", __name__)
if __name__ == "__main__":
    main()

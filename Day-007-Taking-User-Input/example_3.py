# Day 007 · Taking User Input — Several values in one line
# Run: python example_3.py

# Type something like: 10 20 30
data = input("Enter numbers separated by space: ")
numbers = [int(x) for x in data.split()]
print("You entered:", numbers)
print("Total:", sum(numbers))

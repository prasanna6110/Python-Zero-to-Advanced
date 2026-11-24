# 033 · Lambda Functions — Example 3: Lambdas returned from functions
# Run: python example_3.py

def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
triple = multiplier(3)
print(double(10), triple(10))

ops = {"+": lambda a, b: a + b, "-": lambda a, b: a - b,
       "*": lambda a, b: a * b, "/": lambda a, b: a / b}
for op in ops:
    print(f"8 {op} 2 = {ops[op](8, 2)}")

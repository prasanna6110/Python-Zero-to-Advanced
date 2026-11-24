# 013 · while Loops — Example 2: Digit operations
# Run: python example_2.py

n = 98765
total, reverse = 0, 0
temp = n
while temp > 0:
    digit = temp % 10
    total += digit
    reverse = reverse * 10 + digit
    temp //= 10
print("Sum of digits:", total)
print("Reversed:", reverse)

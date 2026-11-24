# Day 038 · Essential Built-in Functions — Maths built-ins
# Run: python example_1.py

print(abs(-7), round(3.14159, 2), pow(2, 10), pow(2, 10, 1000))
print(divmod(17, 5))                # (quotient, remainder)
nums = [4, -9, 2, 7]
print(sum(nums), min(nums), max(nums), max(nums, key=abs))
print(round(2.5), round(3.5))        # banker's rounding: ties go to the nearest even number

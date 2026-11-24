# 067 · Debugging Techniques — Example 2: Debug prints and assertions
# Run: python example_2.py

def average(nums):
    assert len(nums) > 0, "nums must not be empty"
    total = sum(nums)
    print(f"DEBUG {total=} {len(nums)=}")
    return total / len(nums)

print(average([3, 4, 5]))
try:
    average([])
except AssertionError as e:
    print("AssertionError:", e)

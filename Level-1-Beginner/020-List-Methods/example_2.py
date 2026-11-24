# 020 · List Methods — Example 2: Sorting
# Run: python example_2.py

scores = [88, 42, 95, 67, 73]
print(sorted(scores))            # new list
print(scores)                    # unchanged
scores.sort(reverse=True)        # in place
print(scores)
words = ["banana", "Apple", "cherry", "kiwi"]
print(sorted(words, key=str.lower))
print(sorted(words, key=len))

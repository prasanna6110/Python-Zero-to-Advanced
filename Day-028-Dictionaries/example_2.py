# Day 028 · Dictionaries — Word frequency counter
# Run: python example_2.py

text = "the cat and the hat and the bat"
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
print(freq)
most = max(freq, key=freq.get)
print("Most common:", most, freq[most])

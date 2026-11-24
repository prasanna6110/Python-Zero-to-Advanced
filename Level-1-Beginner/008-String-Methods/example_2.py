# 008 · String Methods — Example 2: Searching and replacing
# Run: python example_2.py

s = "I like Java. Java is good."
print(s.find("Java"), s.find("C++"))
print(s.count("Java"))
print(s.replace("Java", "Python"))
print(s.startswith("I"), s.endswith("."))
print("report.pdf".removesuffix(".pdf"))

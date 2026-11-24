# Day 016 · break, continue, pass and loop-else — pass as a placeholder
# Run: python example_2.py

def feature_coming_soon():
    pass               # will be written later

class EmptyModel:
    pass

for i in range(3):
    if i == 1:
        pass           # TODO: handle this case
    else:
        print("Processing", i)
print("pass lets code run before it's finished")

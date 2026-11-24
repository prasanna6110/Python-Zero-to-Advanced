# Day 003 · Keywords, Identifiers, Indentation and Code Structure — All keywords and checking names
# Run: python example_1.py

import keyword

print("Number of keywords:", len(keyword.kwlist))
print(keyword.kwlist)
print("Soft keywords:", keyword.softkwlist)
for name in ["for", "total", "class", "my_var", "2cool", "match"]:
    print(f"{name!r:10} keyword={keyword.iskeyword(name)!s:5} valid identifier={name.isidentifier()}")

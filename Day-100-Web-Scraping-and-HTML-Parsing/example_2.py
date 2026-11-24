# Day 100 · Web Scraping and HTML Parsing — BeautifulSoup (if installed) with a regex fallback
# Run: python example_2.py

import re

HTML = """
<table id="marks">
 <tr><th>Name</th><th>Python</th><th>Maths</th></tr>
 <tr><td>Asha</td><td>91</td><td>85</td></tr>
 <tr><td>Ravi</td><td>78</td><td>92</td></tr>
 <tr><td>Meera</td><td>88</td><td>79</td></tr>
</table>
"""
try:
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(HTML, "html.parser")
    rows = [[td.get_text() for td in tr.find_all(["td", "th"])] for tr in soup.select("#marks tr")]
    print("parsed with BeautifulSoup")
except ImportError:
    print("BeautifulSoup not installed (pip install beautifulsoup4), so using regex instead")
    rows = [re.findall(r"<t[dh]>(.*?)</t[dh]>", tr) for tr in re.findall(r"<tr>(.*?)</tr>", HTML)]

header, *data = rows
for r in data:
    avg = sum(map(int, r[1:])) / len(r[1:])
    print(f"{r[0]:<6} " + "  ".join(f"{h}={v}" for h, v in zip(header[1:], r[1:])) + f"  avg={avg:.1f}")

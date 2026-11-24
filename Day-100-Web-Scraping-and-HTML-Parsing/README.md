# Day 100 · Web Scraping and HTML Parsing

_Advanced_

## What web scraping is
Writing a program that downloads web pages and **pulls data out of them** (prices, news, tables).

## Tools
| Tool | Use |
|------|-----|
| `urllib.request` (stdlib) / **requests** | download pages |
| `html.parser` (stdlib) | a basic HTML parser |
| **BeautifulSoup** (`pip install beautifulsoup4`) | the most popular and easiest parser |
| **lxml**, **parsel** | fast, with XPath and CSS selectors |
| **Selenium** / **Playwright** | pages that need JavaScript |
| **Scrapy** | large crawling projects |

## ⚖️ Scrape ethically
- Read the site's **robots.txt** (`urllib.robotparser`) and its terms of service.
- Add delays and don't overload servers. Set a proper User-Agent.
- Prefer an official **API** if one exists.
- Don't scrape personal data.

> These examples parse HTML stored in the file, so they work offline. Example 3 tries a live request and falls back if there's no internet.

## Examples

### Example 1: Parsing HTML with the standard library  ([`example_1.py`](example_1.py))

```python
from html.parser import HTMLParser

HTML = """
<html><body>
  <h1>Python Books</h1>
  <div class="book"><a href="/b/1">Python Basics</a> <span class="price">₹399</span></div>
  <div class="book"><a href="/b/2">Async Python</a> <span class="price">₹549</span></div>
  <div class="book"><a href="/b/3">Data with Python</a> <span class="price">₹699</span></div>
</body></html>
"""

class BookParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.books, self.current, self.field = [], {}, None
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a":
            self.field, self.current["link"] = "title", attrs["href"]
        elif tag == "span" and attrs.get("class") == "price":
            self.field = "price"
    def handle_data(self, data):
        if self.field:
            self.current[self.field] = data.strip()
            if self.field == "price":
                self.books.append(self.current); self.current = {}
            self.field = None

p = BookParser()
p.feed(HTML)
for b in p.books:
    print(f"{b['title']:<18} {b['price']:>6}  {b['link']}")
```

### Example 2: BeautifulSoup (if installed) with a regex fallback  ([`example_2.py`](example_2.py))

```python
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
```

### Example 3: A polite live request with robots.txt and a fallback  ([`example_3.py`](example_3.py))

```python
import urllib.request, urllib.robotparser, re

URL = "https://www.python.org/"
try:
    rp = urllib.robotparser.RobotFileParser("https://www.python.org/robots.txt")
    rp.read()
    if not rp.can_fetch("CourseBot", URL):
        raise PermissionError("robots.txt disallows this")
    req = urllib.request.Request(URL, headers={"User-Agent": "CourseBot/1.0 (learning)"})
    with urllib.request.urlopen(req, timeout=5) as r:
        html = r.read().decode("utf-8", "ignore")
    print("Live page title:", re.search(r"<title>(.*?)</title>", html, re.S).group(1).strip())
except Exception as e:
    print("No internet or blocked here:", type(e).__name__, "- using a saved sample instead")
    html = "<html><head><title>Welcome to Python.org</title></head></html>"
    print("Sample title:", re.search(r"<title>(.*?)</title>", html).group(1))
```

## Practice

1. Scrape the headlines from a news site's HTML (save the page and parse the saved file).
2. Make a price tracker that warns you when a price drops below a target.
3. Turn an HTML table into a CSV file.

---

[⬅ Day 099](../Day-099-Networking-Sockets-HTTP-and-urllib/README.md) · [🏠 Home](../README.md) · [Day 101 ➡](../Day-101-Sending-Emails-with-smtplib-and-the-email-Package/README.md)

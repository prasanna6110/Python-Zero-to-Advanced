# Day 100 · Web Scraping and HTML Parsing — Parsing HTML with the standard library
# Run: python example_1.py

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

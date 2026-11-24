# Day 100 · Web Scraping and HTML Parsing — A polite live request with robots.txt and a fallback
# Run: python example_3.py

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

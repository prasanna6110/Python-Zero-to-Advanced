# Day 155 · Project: Markdown to HTML Converter — Markdown to HTML
# Run: python main.py

import html
import re
import sys
from pathlib import Path

DEMO = not sys.stdin.isatty()
SAMPLE = """# Day 1: Python Basics
Welcome to **Python Zero to Ultra Advanced** by *Prasanna*.

## What you'll learn
- Variables and `print()`
- Loops and **functions**
- [Python docs](https://docs.python.org)

1. Install Python
2. Run your first program

> Practice every single day!

```python
for day in range(1, 4):
    print(f"Day {day}")
```
---
Made with ❤️ in Kurukshetra
"""

def inline(text):
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', text)
    return text

def convert(md):
    out, list_type, in_code = [], None, False
    def close_list():
        nonlocal list_type
        if list_type:
            out.append(f"</{list_type}>"); list_type = None
    for line in md.splitlines():
        if line.startswith("```"):
            close_list()
            out.append("</code></pre>" if in_code else f'<pre><code class="{line[3:] or "text"}">')
            in_code = not in_code
            continue
        if in_code:
            out.append(html.escape(line)); continue
        if m := re.match(r"(#{1,6}) (.*)", line):
            close_list(); n = len(m.group(1)); out.append(f"<h{n}>{inline(m.group(2))}</h{n}>")
        elif m := re.match(r"[-*] (.*)", line):
            if list_type != "ul": close_list(); out.append("<ul>"); list_type = "ul"
            out.append(f"  <li>{inline(m.group(1))}</li>")
        elif m := re.match(r"\d+\. (.*)", line):
            if list_type != "ol": close_list(); out.append("<ol>"); list_type = "ol"
            out.append(f"  <li>{inline(m.group(1))}</li>")
        elif line.startswith("> "):
            close_list(); out.append(f"<blockquote>{inline(line[2:])}</blockquote>")
        elif line.strip() == "---":
            close_list(); out.append("<hr>")
        elif line.strip():
            close_list(); out.append(f"<p>{inline(line)}</p>")
        else:
            close_list()
    close_list()
    return "\n".join(out)

TEMPLATE = """<!DOCTYPE html><html><head><meta charset="utf-8"><title>{title}</title>
<style>body{{font-family:system-ui;max-width:720px;margin:auto;padding:2rem;line-height:1.6}}
pre{{background:#272822;color:#f8f8f2;padding:1rem;border-radius:8px}} code{{background:#eee;padding:2px 4px}}
pre code{{background:none}} blockquote{{border-left:4px solid #3776ab;margin:0;padding-left:1rem;color:#555}}</style>
</head><body>
{body}
</body></html>"""

if __name__ == "__main__":
    md = SAMPLE if DEMO or len(sys.argv) < 2 else Path(sys.argv[1]).read_text(encoding="utf-8")
    body = convert(md)
    title = re.search(r"<h1>(.*?)</h1>", body).group(1) if "<h1>" in body else "Document"
    page = TEMPLATE.format(title=re.sub("<.*?>", "", title), body=body)
    print(body)
    if not DEMO:
        out = Path(sys.argv[1]).with_suffix(".html") if len(sys.argv) > 1 else Path("output.html")
        out.write_text(page, encoding="utf-8")
        print(f"\n✅ Written to {out}. Open it in your browser!")

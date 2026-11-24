# Day 102 · Working with Excel, PDF and Images (Popular Libraries)

_Advanced_

## The libraries students most often need
| Task | Library | Install |
|------|---------|---------|
| Excel `.xlsx` | **openpyxl** (or pandas) | `pip install openpyxl` |
| Word `.docx` | **python-docx** | `pip install python-docx` |
| PDF read and merge | **pypdf** | `pip install pypdf` |
| PDF create | **reportlab** / **fpdf2** | `pip install fpdf2` |
| Images | **Pillow** | `pip install pillow` |
| Charts | **matplotlib** | `pip install matplotlib` |
| HTTP | **requests** | `pip install requests` |

## A pattern you'll see in these examples
```python
try:
    import openpyxl
except ImportError:
    print("pip install openpyxl")
```
The examples show the real library code, and if it isn't installed they fall back to the standard library so they still run.

## Examples

### Example 1: Excel with openpyxl (CSV fallback)  ([`example_1.py`](example_1.py))

```python
import csv, os

rows = [["Name", "Python", "Maths"], ["Asha", 91, 85], ["Ravi", 78, 92], ["Meera", 88, 79]]
try:
    from openpyxl import Workbook, load_workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Marks"
    for r in rows:
        ws.append(r)
    ws["D1"] = "Total"
    for i in range(2, len(rows) + 1):
        ws[f"D{i}"] = f"=B{i}+C{i}"            # a real Excel formula
    wb.save("marks.xlsx")
    ws2 = load_workbook("marks.xlsx").active
    print("Excel rows:", [[c.value for c in row] for row in ws2.iter_rows()])
    os.remove("marks.xlsx")
except ImportError:
    print("openpyxl not installed (pip install openpyxl). Writing a CSV instead:")
    with open("marks.csv", "w", newline="") as f:
        csv.writer(f).writerows([r + ["Total" if i == 0 else r[1] + r[2]] for i, r in enumerate(rows)])
    print(open("marks.csv").read())
    os.remove("marks.csv")
```

### Example 2: Images with Pillow (pure Python PPM fallback)  ([`example_2.py`](example_2.py))

```python
import os

try:
    from PIL import Image, ImageDraw, ImageFilter
    img = Image.new("RGB", (200, 100), "white")
    d = ImageDraw.Draw(img)
    d.rectangle([20, 20, 180, 80], outline="navy", width=4)
    d.text((55, 45), "Day by Day", fill="black")
    img.filter(ImageFilter.BLUR).resize((100, 50)).save("thumb.png")
    print("Created thumb.png:", Image.open("thumb.png").size)
    os.remove("thumb.png")
except ImportError:
    print("Pillow not installed (pip install pillow). Writing a gradient as a PPM image by hand:")
    w, h = 64, 32
    with open("gradient.ppm", "wb") as f:
        f.write(f"P6 {w} {h} 255\n".encode())
        for y in range(h):
            for x in range(w):
                f.write(bytes([x * 4, y * 8, 128]))
    print("gradient.ppm size:", os.path.getsize("gradient.ppm"), "bytes")
    os.remove("gradient.ppm")
```

### Example 3: Charts with matplotlib (text chart fallback)  ([`example_3.py`](example_3.py))

```python
import os

months = ["Jul", "Aug", "Sep", "Oct", "Nov"]
hours = [12, 20, 26, 31, 40]
try:
    import matplotlib
    matplotlib.use("Agg")                        # save to a file without opening a window
    import matplotlib.pyplot as plt
    plt.plot(months, hours, marker="o")
    plt.title("Python practice hours"); plt.ylabel("hours")
    plt.savefig("progress.png", dpi=80)
    print("Saved progress.png")
    os.remove("progress.png")
except ImportError:
    print("matplotlib not installed (pip install matplotlib). Text chart:")
    for m, h in zip(months, hours):
        print(f"{m} {'█' * (h // 2)} {h}")
```

## Practice

1. Read an Excel sheet of marks and write the grades into a new column.
2. Batch-resize every image in a folder to 800px wide.
3. Plot your weekly study hours as a bar chart.

---

[⬅ Day 101](../Day-101-Sending-Emails-with-smtplib-and-the-email-Package/README.md) · [🏠 Home](../README.md) · [Day 103 ➡](../Day-103-subprocess-Running-System-Commands/README.md)

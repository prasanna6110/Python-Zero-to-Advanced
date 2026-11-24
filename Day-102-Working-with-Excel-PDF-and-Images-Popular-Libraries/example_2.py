# Day 102 · Working with Excel, PDF and Images (Popular Libraries) — Images with Pillow (pure Python PPM fallback)
# Run: python example_2.py

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

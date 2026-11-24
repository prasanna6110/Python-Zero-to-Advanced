# Day 066 · ZIP Archives and Temporary Files — Temporary files
# Run: python example_3.py

import tempfile, os

with tempfile.NamedTemporaryFile("w+", suffix=".txt", delete=False) as f:
    f.write("temporary data")
    path = f.name
print("temp file:", os.path.basename(path), "exists:", os.path.exists(path))
os.remove(path)

with tempfile.TemporaryDirectory() as d:
    print("temp dir exists inside the with:", os.path.isdir(d))
print("temp dir exists after the with:", os.path.isdir(d))
print("system temp folder:", tempfile.gettempdir())

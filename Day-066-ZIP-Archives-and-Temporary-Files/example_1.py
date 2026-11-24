# Day 066 · ZIP Archives and Temporary Files — Creating and reading a zip file
# Run: python example_1.py

import zipfile, tempfile, pathlib

with tempfile.TemporaryDirectory() as tmp:
    folder = pathlib.Path(tmp)
    (folder / "notes.txt").write_text("Python notes " * 100)
    (folder / "code.py").write_text("print('hi')\n" * 50)
    zip_path = folder / "backup.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for f in ["notes.txt", "code.py"]:
            z.write(folder / f, arcname=f)
        z.writestr("readme.md", "# Backup\n")
    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            print(f"{info.filename:<10} {info.file_size:>6} -> {info.compress_size:>4} bytes")
        print(z.read("readme.md").decode())

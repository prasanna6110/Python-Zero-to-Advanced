# Day 066 · ZIP Archives and Temporary Files

_Intermediate_

## zipfile
```python
with zipfile.ZipFile("out.zip", "w", zipfile.ZIP_DEFLATED) as z:
    z.write("file.txt")
    z.writestr("note.txt", "text")
with zipfile.ZipFile("out.zip") as z:
    z.namelist(); z.extractall("folder"); z.read("note.txt")
```
## tarfile, gzip and shutil.make_archive
- `shutil.make_archive("backup", "zip", folder)` zips a whole folder in one line.
- `gzip.open()` reads and writes compressed files (`.gz`).

## tempfile
Gives you temporary files and folders that clean up after themselves:
- `tempfile.TemporaryDirectory()` is a folder that's deleted when the `with` block ends.
- `tempfile.NamedTemporaryFile()` is a temporary file.
- `tempfile.gettempdir()` tells you the system's temp folder.

## Examples

### Example 1: Creating and reading a zip file  ([`example_1.py`](example_1.py))

```python
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
```

### Example 2: Backing up a folder with make_archive and gzip  ([`example_2.py`](example_2.py))

```python
import shutil, tempfile, pathlib, gzip

with tempfile.TemporaryDirectory() as tmp:
    project = pathlib.Path(tmp, "project")
    (project / "src").mkdir(parents=True)
    (project / "src" / "app.py").write_text("print('app')\n")
    (project / "data.csv").write_text("a,b\n1,2\n")
    archive = shutil.make_archive(str(pathlib.Path(tmp, "project_backup")), "zip", project)
    print("created:", pathlib.Path(archive).name)
    shutil.unpack_archive(archive, pathlib.Path(tmp, "restored"))
    print("restored files:", sorted(p.name for p in pathlib.Path(tmp, "restored").rglob("*")))

    gz = pathlib.Path(tmp, "log.txt.gz")
    with gzip.open(gz, "wt") as f:
        f.write("log line\n" * 1000)
    print("gzip size:", gz.stat().st_size, "bytes for 9000 characters")
```

### Example 3: Temporary files  ([`example_3.py`](example_3.py))

```python
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
```

## Practice

1. Write a script that zips every `.py` file in a folder, with a date in the zip's name.
2. Extract a single file from a zip without extracting all of them.
3. Compress a large log file with gzip and compare the sizes.

---

[⬅ Day 065](../Day-065-os-shutil-and-pathlib/README.md) · [🏠 Home](../README.md) · [Day 067 ➡](../Day-067-sys-and-argparse-Command-Line-Programs/README.md)

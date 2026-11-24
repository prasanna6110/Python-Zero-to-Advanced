# Day 066 · ZIP Archives and Temporary Files — Backing up a folder with make_archive and gzip
# Run: python example_2.py

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

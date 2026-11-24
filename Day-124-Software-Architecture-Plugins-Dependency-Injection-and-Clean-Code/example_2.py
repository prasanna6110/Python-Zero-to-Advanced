# Day 124 · Software Architecture: Plugins, Dependency Injection and Clean Code — Plugin discovery from a folder and entry points
# Run: python example_2.py

import importlib.util, pathlib, shutil, importlib.metadata as md

plugin_dir = pathlib.Path("plugins_demo")
plugin_dir.mkdir(exist_ok=True)
(plugin_dir / "uppercase.py").write_text("NAME='upper'\ndef apply(t): return t.upper()\n")
(plugin_dir / "reverse.py").write_text("NAME='reverse'\ndef apply(t): return t[::-1]\n")
(plugin_dir / "exclaim.py").write_text("NAME='exclaim'\ndef apply(t): return t + '!!!'\n")

def discover(folder):
    plugins = {}
    for file in sorted(folder.glob("*.py")):
        spec = importlib.util.spec_from_file_location(file.stem, file)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        if hasattr(mod, "apply"):
            plugins[mod.NAME] = mod.apply
    return plugins

plugins = discover(plugin_dir)
text = "python plugins"
for name, fn in plugins.items():
    text = fn(text)
    print(f"after {name:<8}: {text}")
shutil.rmtree(plugin_dir)

groups = md.entry_points()
print("installed console_scripts (first 5):", [ep.name for ep in groups.select(group="console_scripts")][:5])

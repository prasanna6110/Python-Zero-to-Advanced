# 050 · Advanced Decorators: Arguments, Classes and functools.wraps — Example 3: Class decorators and a registry
# Run: python example_3.py

PLUGINS = {}

def register(name):
    def decorator(cls):
        PLUGINS[name] = cls
        cls.plugin_name = name
        return cls
    return decorator

@register("csv")
class CSVExporter:
    def export(self, rows): return "\n".join(",".join(map(str, r)) for r in rows)

@register("tsv")
class TSVExporter:
    def export(self, rows): return "\n".join("\t".join(map(str, r)) for r in rows)

data = [(1, "a"), (2, "b")]
for name, cls in PLUGINS.items():
    print(f"[{name}]\n{cls().export(data)}")

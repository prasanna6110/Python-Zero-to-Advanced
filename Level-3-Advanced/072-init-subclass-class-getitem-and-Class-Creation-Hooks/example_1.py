# 072 · __init_subclass__, __class_getitem__ and Class Creation Hooks — Example 1: A plugin registry with __init_subclass__
# Run: python example_1.py

class Exporter:
    registry = {}

    def __init_subclass__(cls, /, fmt=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if fmt is None:
            raise TypeError(f"{cls.__name__} needs fmt=...")
        Exporter.registry[fmt] = cls

    @classmethod
    def for_format(cls, fmt):
        return cls.registry[fmt]()

class JSONExporter(Exporter, fmt="json"):
    def export(self, d): return str(d).replace("'", '"')

class XMLExporter(Exporter, fmt="xml"):
    def export(self, d): return "".join(f"<{k}>{v}</{k}>" for k, v in d.items())

data = {"name": "Asha", "age": 21}
for fmt in Exporter.registry:
    print(fmt, "->", Exporter.for_format(fmt).export(data))

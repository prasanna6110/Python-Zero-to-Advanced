# 🐍 Python: Zero to Ultra Advanced

A complete, step-by-step Python course that takes you from **your very first `print()`** all the way to **metaclasses, asyncio internals, the import system, AST manipulation and CPython internals**.

**114 topics · 342 runnable examples · 4 levels**

Every topic folder has:

- 📖 **`README.md`**: simple notes that explain the concept, the syntax and the key points to remember
- 💻 **`example_1.py`, `example_2.py`, `example_3.py`**: small programs you can run, going from easy to more realistic
- 🏋️ **Practice**: questions at the end of each topic so you can test yourself

## 🗺️ How to use this course

1. **Install Python 3.12+** from [python.org](https://www.python.org/downloads/). Tick *"Add Python to PATH"* on Windows.
2. Clone the repo:
   ```bash
   git clone https://github.com/prasanna6110/Python-Zero-to-Ultra-Advanced.git
   cd Python-Zero-to-Ultra-Advanced
   ```
3. Go through the topics **in order**. Each one builds on the one before it.
4. For every topic, read the `README.md`, run each example, **change the code and break it**, then do the practice questions.
   ```bash
   cd Level-1-Beginner/001-Introduction-to-Python
   python example_1.py
   ```
5. Don't rush. Understanding beats speed. If a topic feels hard, re-run its examples and change them until they make sense.

## 🎯 Levels

| Level | What you learn | Who it's for |
|-------|----------------|--------------|
| **1 · Beginner** | Syntax, variables, strings, conditions, loops, functions, collections, files, errors, modules | Absolute beginners |
| **2 · Intermediate** | OOP, iterators, generators, decorators, context managers, standard library, testing, logging | Comfortable with the basics |
| **3 · Advanced** | Descriptors, metaclasses, typing, concurrency, asyncio, memory, performance, databases, networking, DSA, design patterns | Building real projects |
| **4 · Ultra Advanced** | Coroutine internals, writing an event loop, import hooks, AST, bytecode, ctypes, buffer protocol, contextvars, new Python features, capstone projects | Aiming for expert level |

> All examples use only the **Python standard library**, so nothing extra needs to be installed. The few topics that mention third-party libraries still run without them.

## 👤 Author

**Prasanna Kumar Pandey**, NIT Kurukshetra · GitHub: [@prasanna6110](https://github.com/prasanna6110)

If this course helps you, please ⭐ star the repo!

# 📚 Course Contents

## Level 1 — Beginner

_Learn the building blocks: syntax, variables, strings, decisions, loops and your first functions._

| # | Topic | Examples |
|---|-------|----------|
| 001 | [Introduction to Python](Level-1-Beginner/001-Introduction-to-Python/README.md) | 3 |
| 002 | [print(), Comments and Escape Sequences](Level-1-Beginner/002-print-Comments-and-Escape-Sequences/README.md) | 3 |
| 003 | [Variables and Data Types](Level-1-Beginner/003-Variables-and-Data-Types/README.md) | 3 |
| 004 | [Type Casting](Level-1-Beginner/004-Type-Casting/README.md) | 3 |
| 005 | [Taking User Input](Level-1-Beginner/005-Taking-User-Input/README.md) | 3 |
| 006 | [Operators](Level-1-Beginner/006-Operators/README.md) | 3 |
| 007 | [Strings Basics: Indexing and Slicing](Level-1-Beginner/007-Strings-Basics-Indexing-and-Slicing/README.md) | 3 |
| 008 | [String Methods](Level-1-Beginner/008-String-Methods/README.md) | 3 |
| 009 | [String Formatting](Level-1-Beginner/009-String-Formatting/README.md) | 3 |
| 010 | [Conditional Statements: if, elif, else](Level-1-Beginner/010-Conditional-Statements-if-elif-else/README.md) | 3 |
| 011 | [match-case (Structural Pattern Matching)](Level-1-Beginner/011-match-case-Structural-Pattern-Matching/README.md) | 3 |
| 012 | [for Loops and range()](Level-1-Beginner/012-for-Loops-and-range/README.md) | 3 |
| 013 | [while Loops](Level-1-Beginner/013-while-Loops/README.md) | 3 |
| 014 | [break, continue, pass and loop-else](Level-1-Beginner/014-break-continue-pass-and-loop-else/README.md) | 3 |
| 015 | [Functions Basics](Level-1-Beginner/015-Functions-Basics/README.md) | 3 |
| 016 | [Function Arguments in Depth](Level-1-Beginner/016-Function-Arguments-in-Depth/README.md) | 3 |
| 017 | [Scope: LEGB, global and nonlocal](Level-1-Beginner/017-Scope-LEGB-global-and-nonlocal/README.md) | 3 |
| 018 | [Recursion](Level-1-Beginner/018-Recursion/README.md) | 3 |
| 019 | [Lists](Level-1-Beginner/019-Lists/README.md) | 3 |
| 020 | [List Methods](Level-1-Beginner/020-List-Methods/README.md) | 3 |
| 021 | [Tuples](Level-1-Beginner/021-Tuples/README.md) | 3 |
| 022 | [Sets](Level-1-Beginner/022-Sets/README.md) | 3 |
| 023 | [Dictionaries](Level-1-Beginner/023-Dictionaries/README.md) | 3 |
| 024 | [Comprehensions: list, dict and set](Level-1-Beginner/024-Comprehensions-list-dict-and-set/README.md) | 3 |
| 025 | [Mutable vs Immutable and Copying](Level-1-Beginner/025-Mutable-vs-Immutable-and-Copying/README.md) | 3 |
| 026 | [Docstrings and PEP 8 (Writing Clean Code)](Level-1-Beginner/026-Docstrings-and-PEP-8-Writing-Clean-Code/README.md) | 3 |
| 027 | [Exception Handling: try, except, else, finally](Level-1-Beginner/027-Exception-Handling-try-except-else-finally/README.md) | 3 |
| 028 | [Raising Exceptions and Custom Exceptions](Level-1-Beginner/028-Raising-Exceptions-and-Custom-Exceptions/README.md) | 3 |
| 029 | [File Handling](Level-1-Beginner/029-File-Handling/README.md) | 3 |
| 030 | [Modules, Imports and __name__](Level-1-Beginner/030-Modules-Imports-and-name/README.md) | 3 |
| 031 | [Packages, pip and Virtual Environments](Level-1-Beginner/031-Packages-pip-and-Virtual-Environments/README.md) | 3 |
| 032 | [Essential Built-in Functions](Level-1-Beginner/032-Essential-Built-in-Functions/README.md) | 3 |
| 033 | [Lambda Functions](Level-1-Beginner/033-Lambda-Functions/README.md) | 3 |
| 034 | [map, filter and reduce](Level-1-Beginner/034-map-filter-and-reduce/README.md) | 3 |

## Level 2 — Intermediate

_Object-oriented programming, iterators, generators, decorators, the standard library and testing._

| # | Topic | Examples |
|---|-------|----------|
| 035 | [Classes and Objects](Level-2-Intermediate/035-Classes-and-Objects/README.md) | 3 |
| 036 | [Constructors, Instance and Class Attributes](Level-2-Intermediate/036-Constructors-Instance-and-Class-Attributes/README.md) | 3 |
| 037 | [Instance, Class and Static Methods](Level-2-Intermediate/037-Instance-Class-and-Static-Methods/README.md) | 3 |
| 038 | [Inheritance](Level-2-Intermediate/038-Inheritance/README.md) | 3 |
| 039 | [Multiple Inheritance, MRO and super()](Level-2-Intermediate/039-Multiple-Inheritance-MRO-and-super/README.md) | 3 |
| 040 | [Encapsulation, Name Mangling and Properties](Level-2-Intermediate/040-Encapsulation-Name-Mangling-and-Properties/README.md) | 3 |
| 041 | [Polymorphism and Duck Typing](Level-2-Intermediate/041-Polymorphism-and-Duck-Typing/README.md) | 3 |
| 042 | [Abstract Classes and Interfaces (abc)](Level-2-Intermediate/042-Abstract-Classes-and-Interfaces-abc/README.md) | 3 |
| 043 | [Magic (Dunder) Methods and Operator Overloading](Level-2-Intermediate/043-Magic-Dunder-Methods-and-Operator-Overloading/README.md) | 3 |
| 044 | [Dataclasses](Level-2-Intermediate/044-Dataclasses/README.md) | 3 |
| 045 | [Enums](Level-2-Intermediate/045-Enums/README.md) | 3 |
| 046 | [Iterators and the Iterator Protocol](Level-2-Intermediate/046-Iterators-and-the-Iterator-Protocol/README.md) | 3 |
| 047 | [Generators and yield](Level-2-Intermediate/047-Generators-and-yield/README.md) | 3 |
| 048 | [Closures](Level-2-Intermediate/048-Closures/README.md) | 3 |
| 049 | [Decorators](Level-2-Intermediate/049-Decorators/README.md) | 3 |
| 050 | [Advanced Decorators: Arguments, Classes and functools.wraps](Level-2-Intermediate/050-Advanced-Decorators-Arguments-Classes-and-functools-wraps/README.md) | 3 |
| 051 | [Context Managers (with and contextlib)](Level-2-Intermediate/051-Context-Managers-with-and-contextlib/README.md) | 3 |
| 052 | [Type Hints Basics](Level-2-Intermediate/052-Type-Hints-Basics/README.md) | 3 |
| 053 | [Walrus Operator, Unpacking and Star Expressions](Level-2-Intermediate/053-Walrus-Operator-Unpacking-and-Star-Expressions/README.md) | 3 |
| 054 | [Advanced Sorting](Level-2-Intermediate/054-Advanced-Sorting/README.md) | 3 |
| 055 | [datetime and Time Zones](Level-2-Intermediate/055-datetime-and-Time-Zones/README.md) | 3 |
| 056 | [math, random and statistics](Level-2-Intermediate/056-math-random-and-statistics/README.md) | 3 |
| 057 | [os, shutil and pathlib](Level-2-Intermediate/057-os-shutil-and-pathlib/README.md) | 3 |
| 058 | [sys and argparse: Command-Line Programs](Level-2-Intermediate/058-sys-and-argparse-Command-Line-Programs/README.md) | 3 |
| 059 | [JSON and CSV](Level-2-Intermediate/059-JSON-and-CSV/README.md) | 3 |
| 060 | [Regular Expressions (re)](Level-2-Intermediate/060-Regular-Expressions-re/README.md) | 3 |
| 061 | [collections Module](Level-2-Intermediate/061-collections-Module/README.md) | 3 |
| 062 | [itertools](Level-2-Intermediate/062-itertools/README.md) | 3 |
| 063 | [functools](Level-2-Intermediate/063-functools/README.md) | 3 |
| 064 | [Logging](Level-2-Intermediate/064-Logging/README.md) | 3 |
| 065 | [Unit Testing with unittest](Level-2-Intermediate/065-Unit-Testing-with-unittest/README.md) | 3 |
| 066 | [pytest and doctest](Level-2-Intermediate/066-pytest-and-doctest/README.md) | 3 |
| 067 | [Debugging Techniques](Level-2-Intermediate/067-Debugging-Techniques/README.md) | 3 |
| 068 | [Bytes, Encoding and Unicode](Level-2-Intermediate/068-Bytes-Encoding-and-Unicode/README.md) | 3 |

## Level 3 — Advanced

_Deep OOP, typing, concurrency, asyncio, memory and performance._

| # | Topic | Examples |
|---|-------|----------|
| 069 | [__new__ vs __init__ and __slots__](Level-3-Advanced/069-new-vs-init-and-slots/README.md) | 3 |
| 070 | [Descriptors](Level-3-Advanced/070-Descriptors/README.md) | 3 |
| 071 | [Metaclasses](Level-3-Advanced/071-Metaclasses/README.md) | 3 |
| 072 | [__init_subclass__, __class_getitem__ and Class Creation Hooks](Level-3-Advanced/072-init-subclass-class-getitem-and-Class-Creation-Hooks/README.md) | 3 |
| 073 | [Advanced Type Hints: Generics, Protocols and More](Level-3-Advanced/073-Advanced-Type-Hints-Generics-Protocols-and-More/README.md) | 3 |
| 074 | [Threading](Level-3-Advanced/074-Threading/README.md) | 3 |
| 075 | [Multiprocessing](Level-3-Advanced/075-Multiprocessing/README.md) | 3 |
| 076 | [concurrent.futures](Level-3-Advanced/076-concurrent-futures/README.md) | 3 |
| 077 | [asyncio Basics](Level-3-Advanced/077-asyncio-Basics/README.md) | 3 |
| 078 | [asyncio Advanced: Tasks, Timeouts, Queues and Semaphores](Level-3-Advanced/078-asyncio-Advanced-Tasks-Timeouts-Queues-and-Semaphores/README.md) | 3 |
| 079 | [The GIL and Choosing the Right Concurrency Model](Level-3-Advanced/079-The-GIL-and-Choosing-the-Right-Concurrency-Model/README.md) | 3 |
| 080 | [Memory Management, Garbage Collection and weakref](Level-3-Advanced/080-Memory-Management-Garbage-Collection-and-weakref/README.md) | 3 |
| 081 | [Python Internals: Bytecode and dis](Level-3-Advanced/081-Python-Internals-Bytecode-and-dis/README.md) | 3 |
| 082 | [Introspection and Reflection (inspect, getattr)](Level-3-Advanced/082-Introspection-and-Reflection-inspect-getattr/README.md) | 3 |
| 083 | [Performance: Profiling and Optimisation](Level-3-Advanced/083-Performance-Profiling-and-Optimisation/README.md) | 3 |
| 084 | [Packaging and Distributing Your Code](Level-3-Advanced/084-Packaging-and-Distributing-Your-Code/README.md) | 3 |
| 085 | [Design Patterns in Python](Level-3-Advanced/085-Design-Patterns-in-Python/README.md) | 3 |
| 086 | [Functional Programming in Python](Level-3-Advanced/086-Functional-Programming-in-Python/README.md) | 3 |
| 087 | [Serialization: pickle, shelve and struct](Level-3-Advanced/087-Serialization-pickle-shelve-and-struct/README.md) | 3 |
| 088 | [Databases with sqlite3](Level-3-Advanced/088-Databases-with-sqlite3/README.md) | 3 |
| 089 | [Networking: Sockets, HTTP and urllib](Level-3-Advanced/089-Networking-Sockets-HTTP-and-urllib/README.md) | 3 |
| 090 | [subprocess: Running System Commands](Level-3-Advanced/090-subprocess-Running-System-Commands/README.md) | 3 |
| 091 | [Security Basics: hashing, secrets and hmac](Level-3-Advanced/091-Security-Basics-hashing-secrets-and-hmac/README.md) | 3 |
| 092 | [heapq, bisect and array](Level-3-Advanced/092-heapq-bisect-and-array/README.md) | 3 |
| 093 | [Data Structures from Scratch](Level-3-Advanced/093-Data-Structures-from-Scratch/README.md) | 3 |
| 094 | [Algorithms: Searching and Sorting](Level-3-Advanced/094-Algorithms-Searching-and-Sorting/README.md) | 3 |
| 095 | [Algorithms: Graphs, Recursion Patterns and Dynamic Programming](Level-3-Advanced/095-Algorithms-Graphs-Recursion-Patterns-and-Dynamic-Programming/README.md) | 3 |

## Level 4 — Ultra Advanced

_CPython internals, coroutine machinery, the import system, AST, C interop and expert-level patterns._

| # | Topic | Examples |
|---|-------|----------|
| 096 | [Generator Internals: send, throw, close and yield from](Level-4-Ultra-Advanced/096-Generator-Internals-send-throw-close-and-yield-from/README.md) | 3 |
| 097 | [Build Your Own Event Loop (How async Really Works)](Level-4-Ultra-Advanced/097-Build-Your-Own-Event-Loop-How-async-Really-Works/README.md) | 3 |
| 098 | [Async Iterators, Async Generators and Async Context Managers](Level-4-Ultra-Advanced/098-Async-Iterators-Async-Generators-and-Async-Context-Managers/README.md) | 3 |
| 099 | [contextvars: Context-Local State](Level-4-Ultra-Advanced/099-contextvars-Context-Local-State/README.md) | 3 |
| 100 | [The Import System: importlib and Import Hooks](Level-4-Ultra-Advanced/100-The-Import-System-importlib-and-Import-Hooks/README.md) | 3 |
| 101 | [AST: Parsing, Analysing and Transforming Code](Level-4-Ultra-Advanced/101-AST-Parsing-Analysing-and-Transforming-Code/README.md) | 3 |
| 102 | [Advanced Metaprogramming: Code Generation and Function Objects](Level-4-Ultra-Advanced/102-Advanced-Metaprogramming-Code-Generation-and-Function-Objects/README.md) | 3 |
| 103 | [ctypes: Calling C from Python](Level-4-Ultra-Advanced/103-ctypes-Calling-C-from-Python/README.md) | 3 |
| 104 | [The Buffer Protocol and memoryview](Level-4-Ultra-Advanced/104-The-Buffer-Protocol-and-memoryview/README.md) | 3 |
| 105 | [Mocking and Monkey Patching (unittest.mock)](Level-4-Ultra-Advanced/105-Mocking-and-Monkey-Patching-unittest-mock/README.md) | 3 |
| 106 | [Modern Python Features (3.10 to 3.13)](Level-4-Ultra-Advanced/106-Modern-Python-Features-3-10-to-3-13/README.md) | 3 |
| 107 | [Advanced Structural Pattern Matching](Level-4-Ultra-Advanced/107-Advanced-Structural-Pattern-Matching/README.md) | 3 |
| 108 | [Tracing, Profiling Hooks and Audit Hooks](Level-4-Ultra-Advanced/108-Tracing-Profiling-Hooks-and-Audit-Hooks/README.md) | 3 |
| 109 | [Advanced Concurrency Patterns](Level-4-Ultra-Advanced/109-Advanced-Concurrency-Patterns/README.md) | 3 |
| 110 | [Build a Mini Programming Language (Interpreter)](Level-4-Ultra-Advanced/110-Build-a-Mini-Programming-Language-Interpreter/README.md) | 3 |
| 111 | [Software Architecture: Plugins, Dependency Injection and Clean Code](Level-4-Ultra-Advanced/111-Software-Architecture-Plugins-Dependency-Injection-and-Clean-Code/README.md) | 3 |
| 112 | [The Python Ecosystem Roadmap](Level-4-Ultra-Advanced/112-The-Python-Ecosystem-Roadmap/README.md) | 3 |
| 113 | [Capstone Projects I: Applications](Level-4-Ultra-Advanced/113-Capstone-Projects-I-Applications/README.md) | 3 |
| 114 | [Capstone Projects II: Systems](Level-4-Ultra-Advanced/114-Capstone-Projects-II-Systems/README.md) | 3 |

---

Made with ❤️ by **Prasanna Kumar Pandey** · [github.com/prasanna6110](https://github.com/prasanna6110)

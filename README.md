# 🐍 Python: Zero to Ultra Advanced (Day-wise)

A complete **day-by-day** Python course. It starts with **your very first `print()`** and goes all the way to **metaclasses, asyncio internals, import hooks, AST and CPython internals**, then finishes with **48 real projects**.

**176 days · 432 runnable code files · 48 projects**

Do **one day at a time**. Every day folder has:

- 📖 **`README.md`**: easy notes (what it is, why it matters, the syntax, the key points)
- 💻 **`example_1.py`, `example_2.py`, `example_3.py`**: runnable programs that go from easy to realistic
- 🏋️ **Practice**: questions so you can test yourself
- ⬅ ➡ links at the bottom to jump to the previous or next day

The project days have a `main.py` you can run, plus ideas for extending the project.

## 🗺️ How to follow this course

1. **Install Python 3.12+** from [python.org](https://www.python.org/downloads/). On Windows, tick *"Add Python to PATH"*. Install **VS Code** with the Python extension.
2. Get the code:
   ```bash
   git clone https://github.com/prasanna6110/Python-Zero-to-Ultra-Advanced.git
   cd Python-Zero-to-Ultra-Advanced
   ```
3. Start at **[Day 001](Day-001-Introduction-to-Python/README.md)** and go in order. Each day builds on the one before it.
4. Every day: **read** the README → **run** each example → **change** the code and break it → **solve** the practice questions.
   ```bash
   cd Day-001-Introduction-to-Python
   python example_1.py
   ```
5. Stuck? Re-read the notes, add `print()` statements, and look at the **Interview Questions** and **Common Mistakes** days.

## 🎯 Phases

| Phase | What you learn |
|-------|----------------|
| **Beginner** | Syntax, variables, numbers, strings, conditions, loops, pattern printing, functions, collections, files, errors, modules, classic programs |
| **Intermediate** | OOP, iterators, generators, decorators, context managers, standard library, GUI, testing, logging |
| **Advanced** | Descriptors, metaclasses, typing, concurrency, asyncio, memory, performance, databases, networking, web scraping, DSA, design patterns |
| **Ultra Advanced** | Coroutine internals, your own event loop, import hooks, AST, bytecode, ctypes, buffer protocol, new Python features, interview prep |
| **Projects** | 48 projects: games, tools, management systems, servers, ML from scratch and more |

> Everything uses the **Python standard library**, so no extra installs are needed. The few days that mention NumPy, pandas, requests or Tkinter still run (or explain what to install) if those are missing.

## 💡 Running the projects

The projects are **interactive**: run `python main.py` in a terminal and play. When their input isn't coming from a terminal (for example, an automated test), they switch to **demo mode** and play themselves.

## 👤 Author

**Prasanna Kumar Pandey**, NIT Kurukshetra · GitHub: [@prasanna6110](https://github.com/prasanna6110)

If this course helps you, please ⭐ star the repo and share it with your friends!

# 📅 Day-wise Contents

## Beginner (Day 1 – Day 40)

_Learn the building blocks: syntax, variables, strings, decisions, loops and your first functions._

| Day | Topic | Files |
|-----|-------|-------|
| 001 | [Introduction to Python](Day-001-Introduction-to-Python/README.md) | 3 |
| 002 | [print(), Comments and Escape Sequences](Day-002-print-Comments-and-Escape-Sequences/README.md) | 3 |
| 003 | [Keywords, Identifiers, Indentation and Code Structure](Day-003-Keywords-Identifiers-Indentation-and-Code-Structure/README.md) | 3 |
| 004 | [Variables and Data Types](Day-004-Variables-and-Data-Types/README.md) | 3 |
| 005 | [Type Casting](Day-005-Type-Casting/README.md) | 3 |
| 006 | [Numbers in Depth: int, float, Decimal, Fraction and complex](Day-006-Numbers-in-Depth-int-float-Decimal-Fraction-and-complex/README.md) | 3 |
| 007 | [Taking User Input](Day-007-Taking-User-Input/README.md) | 3 |
| 008 | [Operators](Day-008-Operators/README.md) | 3 |
| 009 | [Strings Basics: Indexing and Slicing](Day-009-Strings-Basics-Indexing-and-Slicing/README.md) | 3 |
| 010 | [String Methods](Day-010-String-Methods/README.md) | 3 |
| 011 | [String Formatting](Day-011-String-Formatting/README.md) | 3 |
| 012 | [Conditional Statements: if, elif, else](Day-012-Conditional-Statements-if-elif-else/README.md) | 3 |
| 013 | [match-case (Structural Pattern Matching)](Day-013-match-case-Structural-Pattern-Matching/README.md) | 3 |
| 014 | [for Loops and range()](Day-014-for-Loops-and-range/README.md) | 3 |
| 015 | [while Loops](Day-015-while-Loops/README.md) | 3 |
| 016 | [break, continue, pass and loop-else](Day-016-break-continue-pass-and-loop-else/README.md) | 3 |
| 017 | [Nested Loops and Pattern Printing](Day-017-Nested-Loops-and-Pattern-Printing/README.md) | 3 |
| 018 | [Functions Basics](Day-018-Functions-Basics/README.md) | 3 |
| 019 | [Function Arguments in Depth](Day-019-Function-Arguments-in-Depth/README.md) | 3 |
| 020 | [Scope: LEGB, global and nonlocal](Day-020-Scope-LEGB-global-and-nonlocal/README.md) | 3 |
| 021 | [Recursion](Day-021-Recursion/README.md) | 3 |
| 022 | [Classic Number Programs (Exam and Interview Favourites)](Day-022-Classic-Number-Programs-Exam-and-Interview-Favourites/README.md) | 3 |
| 023 | [Classic String Programs](Day-023-Classic-String-Programs/README.md) | 3 |
| 024 | [Lists](Day-024-Lists/README.md) | 3 |
| 025 | [List Methods](Day-025-List-Methods/README.md) | 3 |
| 026 | [Tuples](Day-026-Tuples/README.md) | 3 |
| 027 | [Sets](Day-027-Sets/README.md) | 3 |
| 028 | [Dictionaries](Day-028-Dictionaries/README.md) | 3 |
| 029 | [Comprehensions: list, dict and set](Day-029-Comprehensions-list-dict-and-set/README.md) | 3 |
| 030 | [Classic List and Dictionary Programs](Day-030-Classic-List-and-Dictionary-Programs/README.md) | 3 |
| 031 | [Mutable vs Immutable and Copying](Day-031-Mutable-vs-Immutable-and-Copying/README.md) | 3 |
| 032 | [Docstrings and PEP 8 (Writing Clean Code)](Day-032-Docstrings-and-PEP-8-Writing-Clean-Code/README.md) | 3 |
| 033 | [Exception Handling: try, except, else, finally](Day-033-Exception-Handling-try-except-else-finally/README.md) | 3 |
| 034 | [Raising Exceptions and Custom Exceptions](Day-034-Raising-Exceptions-and-Custom-Exceptions/README.md) | 3 |
| 035 | [File Handling](Day-035-File-Handling/README.md) | 3 |
| 036 | [Modules, Imports and __name__](Day-036-Modules-Imports-and-name/README.md) | 3 |
| 037 | [Packages, pip and Virtual Environments](Day-037-Packages-pip-and-Virtual-Environments/README.md) | 3 |
| 038 | [Essential Built-in Functions](Day-038-Essential-Built-in-Functions/README.md) | 3 |
| 039 | [Lambda Functions](Day-039-Lambda-Functions/README.md) | 3 |
| 040 | [map, filter and reduce](Day-040-map-filter-and-reduce/README.md) | 3 |

## Intermediate (Day 41 – Day 78)

_Object-oriented programming, iterators, generators, decorators, the standard library and testing._

| Day | Topic | Files |
|-----|-------|-------|
| 041 | [Classes and Objects](Day-041-Classes-and-Objects/README.md) | 3 |
| 042 | [Constructors, Instance and Class Attributes](Day-042-Constructors-Instance-and-Class-Attributes/README.md) | 3 |
| 043 | [Instance, Class and Static Methods](Day-043-Instance-Class-and-Static-Methods/README.md) | 3 |
| 044 | [Inheritance](Day-044-Inheritance/README.md) | 3 |
| 045 | [Multiple Inheritance, MRO and super()](Day-045-Multiple-Inheritance-MRO-and-super/README.md) | 3 |
| 046 | [Encapsulation, Name Mangling and Properties](Day-046-Encapsulation-Name-Mangling-and-Properties/README.md) | 3 |
| 047 | [Polymorphism and Duck Typing](Day-047-Polymorphism-and-Duck-Typing/README.md) | 3 |
| 048 | [Composition, Aggregation and Object Relationships](Day-048-Composition-Aggregation-and-Object-Relationships/README.md) | 3 |
| 049 | [Abstract Classes and Interfaces (abc)](Day-049-Abstract-Classes-and-Interfaces-abc/README.md) | 3 |
| 050 | [Magic (Dunder) Methods and Operator Overloading](Day-050-Magic-Dunder-Methods-and-Operator-Overloading/README.md) | 3 |
| 051 | [Dataclasses](Day-051-Dataclasses/README.md) | 3 |
| 052 | [Enums](Day-052-Enums/README.md) | 3 |
| 053 | [Iterators and the Iterator Protocol](Day-053-Iterators-and-the-Iterator-Protocol/README.md) | 3 |
| 054 | [Generators and yield](Day-054-Generators-and-yield/README.md) | 3 |
| 055 | [Closures](Day-055-Closures/README.md) | 3 |
| 056 | [Decorators](Day-056-Decorators/README.md) | 3 |
| 057 | [Advanced Decorators: Arguments, Classes and functools.wraps](Day-057-Advanced-Decorators-Arguments-Classes-and-functools-wraps/README.md) | 3 |
| 058 | [Context Managers (with and contextlib)](Day-058-Context-Managers-with-and-contextlib/README.md) | 3 |
| 059 | [Type Hints Basics](Day-059-Type-Hints-Basics/README.md) | 3 |
| 060 | [Walrus Operator, Unpacking and Star Expressions](Day-060-Walrus-Operator-Unpacking-and-Star-Expressions/README.md) | 3 |
| 061 | [Advanced Sorting](Day-061-Advanced-Sorting/README.md) | 3 |
| 062 | [datetime and Time Zones](Day-062-datetime-and-Time-Zones/README.md) | 3 |
| 063 | [time and calendar Modules](Day-063-time-and-calendar-Modules/README.md) | 3 |
| 064 | [math, random and statistics](Day-064-math-random-and-statistics/README.md) | 3 |
| 065 | [os, shutil and pathlib](Day-065-os-shutil-and-pathlib/README.md) | 3 |
| 066 | [ZIP Archives and Temporary Files](Day-066-ZIP-Archives-and-Temporary-Files/README.md) | 3 |
| 067 | [sys and argparse: Command-Line Programs](Day-067-sys-and-argparse-Command-Line-Programs/README.md) | 3 |
| 068 | [JSON and CSV](Day-068-JSON-and-CSV/README.md) | 3 |
| 069 | [Regular Expressions (re)](Day-069-Regular-Expressions-re/README.md) | 3 |
| 070 | [collections Module](Day-070-collections-Module/README.md) | 3 |
| 071 | [itertools](Day-071-itertools/README.md) | 3 |
| 072 | [functools](Day-072-functools/README.md) | 3 |
| 073 | [Logging](Day-073-Logging/README.md) | 3 |
| 074 | [Unit Testing with unittest](Day-074-Unit-Testing-with-unittest/README.md) | 3 |
| 075 | [pytest and doctest](Day-075-pytest-and-doctest/README.md) | 3 |
| 076 | [Debugging Techniques](Day-076-Debugging-Techniques/README.md) | 3 |
| 077 | [Bytes, Encoding and Unicode](Day-077-Bytes-Encoding-and-Unicode/README.md) | 3 |
| 078 | [GUI Programming with Tkinter](Day-078-GUI-Programming-with-Tkinter/README.md) | 3 |

## Advanced (Day 79 – Day 108)

_Deep OOP, typing, concurrency, asyncio, memory and performance._

| Day | Topic | Files |
|-----|-------|-------|
| 079 | [__new__ vs __init__ and __slots__](Day-079-new-vs-init-and-slots/README.md) | 3 |
| 080 | [Descriptors](Day-080-Descriptors/README.md) | 3 |
| 081 | [Metaclasses](Day-081-Metaclasses/README.md) | 3 |
| 082 | [__init_subclass__, __class_getitem__ and Class Creation Hooks](Day-082-init-subclass-class-getitem-and-Class-Creation-Hooks/README.md) | 3 |
| 083 | [Advanced Type Hints: Generics, Protocols and More](Day-083-Advanced-Type-Hints-Generics-Protocols-and-More/README.md) | 3 |
| 084 | [Threading](Day-084-Threading/README.md) | 3 |
| 085 | [Multiprocessing](Day-085-Multiprocessing/README.md) | 3 |
| 086 | [concurrent.futures](Day-086-concurrent-futures/README.md) | 3 |
| 087 | [asyncio Basics](Day-087-asyncio-Basics/README.md) | 3 |
| 088 | [asyncio Advanced: Tasks, Timeouts, Queues and Semaphores](Day-088-asyncio-Advanced-Tasks-Timeouts-Queues-and-Semaphores/README.md) | 3 |
| 089 | [The GIL and Choosing the Right Concurrency Model](Day-089-The-GIL-and-Choosing-the-Right-Concurrency-Model/README.md) | 3 |
| 090 | [Memory Management, Garbage Collection and weakref](Day-090-Memory-Management-Garbage-Collection-and-weakref/README.md) | 3 |
| 091 | [Python Internals: Bytecode and dis](Day-091-Python-Internals-Bytecode-and-dis/README.md) | 3 |
| 092 | [Introspection and Reflection (inspect, getattr)](Day-092-Introspection-and-Reflection-inspect-getattr/README.md) | 3 |
| 093 | [Performance: Profiling and Optimisation](Day-093-Performance-Profiling-and-Optimisation/README.md) | 3 |
| 094 | [Packaging and Distributing Your Code](Day-094-Packaging-and-Distributing-Your-Code/README.md) | 3 |
| 095 | [Design Patterns in Python](Day-095-Design-Patterns-in-Python/README.md) | 3 |
| 096 | [Functional Programming in Python](Day-096-Functional-Programming-in-Python/README.md) | 3 |
| 097 | [Serialization: pickle, shelve and struct](Day-097-Serialization-pickle-shelve-and-struct/README.md) | 3 |
| 098 | [Databases with sqlite3](Day-098-Databases-with-sqlite3/README.md) | 3 |
| 099 | [Networking: Sockets, HTTP and urllib](Day-099-Networking-Sockets-HTTP-and-urllib/README.md) | 3 |
| 100 | [Web Scraping and HTML Parsing](Day-100-Web-Scraping-and-HTML-Parsing/README.md) | 3 |
| 101 | [Sending Emails with smtplib and the email Package](Day-101-Sending-Emails-with-smtplib-and-the-email-Package/README.md) | 3 |
| 102 | [Working with Excel, PDF and Images (Popular Libraries)](Day-102-Working-with-Excel-PDF-and-Images-Popular-Libraries/README.md) | 3 |
| 103 | [subprocess: Running System Commands](Day-103-subprocess-Running-System-Commands/README.md) | 3 |
| 104 | [Security Basics: hashing, secrets and hmac](Day-104-Security-Basics-hashing-secrets-and-hmac/README.md) | 3 |
| 105 | [heapq, bisect and array](Day-105-heapq-bisect-and-array/README.md) | 3 |
| 106 | [Data Structures from Scratch](Day-106-Data-Structures-from-Scratch/README.md) | 3 |
| 107 | [Algorithms: Searching and Sorting](Day-107-Algorithms-Searching-and-Sorting/README.md) | 3 |
| 108 | [Algorithms: Graphs, Recursion Patterns and Dynamic Programming](Day-108-Algorithms-Graphs-Recursion-Patterns-and-Dynamic-Programming/README.md) | 3 |

## Ultra Advanced (Day 109 – Day 128)

_CPython internals, coroutine machinery, the import system, AST, C interop and expert-level patterns._

| Day | Topic | Files |
|-----|-------|-------|
| 109 | [Generator Internals: send, throw, close and yield from](Day-109-Generator-Internals-send-throw-close-and-yield-from/README.md) | 3 |
| 110 | [Build Your Own Event Loop (How async Really Works)](Day-110-Build-Your-Own-Event-Loop-How-async-Really-Works/README.md) | 3 |
| 111 | [Async Iterators, Async Generators and Async Context Managers](Day-111-Async-Iterators-Async-Generators-and-Async-Context-Managers/README.md) | 3 |
| 112 | [contextvars: Context-Local State](Day-112-contextvars-Context-Local-State/README.md) | 3 |
| 113 | [The Import System: importlib and Import Hooks](Day-113-The-Import-System-importlib-and-Import-Hooks/README.md) | 3 |
| 114 | [AST: Parsing, Analysing and Transforming Code](Day-114-AST-Parsing-Analysing-and-Transforming-Code/README.md) | 3 |
| 115 | [Advanced Metaprogramming: Code Generation and Function Objects](Day-115-Advanced-Metaprogramming-Code-Generation-and-Function-Objects/README.md) | 3 |
| 116 | [ctypes: Calling C from Python](Day-116-ctypes-Calling-C-from-Python/README.md) | 3 |
| 117 | [The Buffer Protocol and memoryview](Day-117-The-Buffer-Protocol-and-memoryview/README.md) | 3 |
| 118 | [Mocking and Monkey Patching (unittest.mock)](Day-118-Mocking-and-Monkey-Patching-unittest-mock/README.md) | 3 |
| 119 | [Modern Python Features (3.10 to 3.13)](Day-119-Modern-Python-Features-3-10-to-3-13/README.md) | 3 |
| 120 | [Advanced Structural Pattern Matching](Day-120-Advanced-Structural-Pattern-Matching/README.md) | 3 |
| 121 | [Tracing, Profiling Hooks and Audit Hooks](Day-121-Tracing-Profiling-Hooks-and-Audit-Hooks/README.md) | 3 |
| 122 | [Advanced Concurrency Patterns](Day-122-Advanced-Concurrency-Patterns/README.md) | 3 |
| 123 | [Build a Mini Programming Language (Interpreter)](Day-123-Build-a-Mini-Programming-Language-Interpreter/README.md) | 3 |
| 124 | [Software Architecture: Plugins, Dependency Injection and Clean Code](Day-124-Software-Architecture-Plugins-Dependency-Injection-and-Clean-Code/README.md) | 3 |
| 125 | [The Python Ecosystem Roadmap](Day-125-The-Python-Ecosystem-Roadmap/README.md) | 3 |
| 126 | [Writing Pythonic Code (Idioms and Best Practices)](Day-126-Writing-Pythonic-Code-Idioms-and-Best-Practices/README.md) | 3 |
| 127 | [Common Mistakes and Gotchas](Day-127-Common-Mistakes-and-Gotchas/README.md) | 3 |
| 128 | [Python Interview Questions (with Answers)](Day-128-Python-Interview-Questions-with-Answers/README.md) | 3 |

## Projects (Day 129 – Day 176)

_Build real projects, from simple games to servers and machine learning from scratch. Each project is one day._

| Day | Topic | Files |
|-----|-------|-------|
| 129 | [Project: Number Guessing Game](Day-129-Project-Number-Guessing-Game/README.md) | 1 |
| 130 | [Project: Rock Paper Scissors](Day-130-Project-Rock-Paper-Scissors/README.md) | 1 |
| 131 | [Project: Menu-Driven Scientific Calculator](Day-131-Project-Menu-Driven-Scientific-Calculator/README.md) | 1 |
| 132 | [Project: Unit Converter](Day-132-Project-Unit-Converter/README.md) | 1 |
| 133 | [Project: Password Generator and Strength Checker](Day-133-Project-Password-Generator-and-Strength-Checker/README.md) | 1 |
| 134 | [Project: Dice Rolling Simulator and Probability Lab](Day-134-Project-Dice-Rolling-Simulator-and-Probability-Lab/README.md) | 1 |
| 135 | [Project: Hangman](Day-135-Project-Hangman/README.md) | 1 |
| 136 | [Project: Tic-Tac-Toe with an Unbeatable AI](Day-136-Project-Tic-Tac-Toe-with-an-Unbeatable-AI/README.md) | 1 |
| 137 | [Project: To-Do List Manager (JSON Storage)](Day-137-Project-To-Do-List-Manager-JSON-Storage/README.md) | 1 |
| 138 | [Project: Contact Book (CSV with Search and Validation)](Day-138-Project-Contact-Book-CSV-with-Search-and-Validation/README.md) | 1 |
| 139 | [Project: Student Report Card System](Day-139-Project-Student-Report-Card-System/README.md) | 1 |
| 140 | [Project: Text Analyzer](Day-140-Project-Text-Analyzer/README.md) | 1 |
| 141 | [Project: Caesar and Vigenère Cipher Tool](Day-141-Project-Caesar-and-Vigenere-Cipher-Tool/README.md) | 1 |
| 142 | [Project: Number System Converter](Day-142-Project-Number-System-Converter/README.md) | 1 |
| 143 | [Project: Shopping Bill Generator with GST](Day-143-Project-Shopping-Bill-Generator-with-GST/README.md) | 1 |
| 144 | [Project: Typing Speed Test](Day-144-Project-Typing-Speed-Test/README.md) | 1 |
| 145 | [Project: Text Adventure Game](Day-145-Project-Text-Adventure-Game/README.md) | 1 |
| 146 | [Project: Python Quiz Engine](Day-146-Project-Python-Quiz-Engine/README.md) | 1 |
| 147 | [Project: Expense Tracker with SQLite](Day-147-Project-Expense-Tracker-with-SQLite/README.md) | 1 |
| 148 | [Project: Library Management System](Day-148-Project-Library-Management-System/README.md) | 1 |
| 149 | [Project: Bank Management System](Day-149-Project-Bank-Management-System/README.md) | 1 |
| 150 | [Project: Movie Ticket Booking System](Day-150-Project-Movie-Ticket-Booking-System/README.md) | 1 |
| 151 | [Project: Inventory Management System (SQLite)](Day-151-Project-Inventory-Management-System-SQLite/README.md) | 1 |
| 152 | [Project: Smart File Organizer](Day-152-Project-Smart-File-Organizer/README.md) | 1 |
| 153 | [Project: Duplicate File Finder](Day-153-Project-Duplicate-File-Finder/README.md) | 1 |
| 154 | [Project: Log File Analyzer](Day-154-Project-Log-File-Analyzer/README.md) | 1 |
| 155 | [Project: Markdown to HTML Converter](Day-155-Project-Markdown-to-HTML-Converter/README.md) | 1 |
| 156 | [Project: URL Shortener (SQLite + Base62)](Day-156-Project-URL-Shortener-SQLite-Base62/README.md) | 1 |
| 157 | [Project: Conway's Game of Life](Day-157-Project-Conway-s-Game-of-Life/README.md) | 1 |
| 158 | [Project: Sudoku Solver and Generator](Day-158-Project-Sudoku-Solver-and-Generator/README.md) | 1 |
| 159 | [Project: Maze Generator and Solver](Day-159-Project-Maze-Generator-and-Solver/README.md) | 1 |
| 160 | [Project: Weather Dashboard (API with an Offline Fallback)](Day-160-Project-Weather-Dashboard-API-with-an-Offline-Fallback/README.md) | 1 |
| 161 | [Project: Loan EMI Calculator with Amortization Schedule](Day-161-Project-Loan-EMI-Calculator-with-Amortization-Schedule/README.md) | 1 |
| 162 | [Project: Key-Value Database Server (Mini Redis)](Day-162-Project-Key-Value-Database-Server-Mini-Redis/README.md) | 1 |
| 163 | [Project: Async Web Crawler](Day-163-Project-Async-Web-Crawler/README.md) | 1 |
| 164 | [Project: Mini Web Framework (like Flask)](Day-164-Project-Mini-Web-Framework-like-Flask/README.md) | 1 |
| 165 | [Project: Multi-Client Chat Server](Day-165-Project-Multi-Client-Chat-Server/README.md) | 1 |
| 166 | [Project: REST API for a To-Do App (http.server + SQLite)](Day-166-Project-REST-API-for-a-To-Do-App-http-server-SQLite/README.md) | 1 |
| 167 | [Project: Blockchain from Scratch](Day-167-Project-Blockchain-from-Scratch/README.md) | 1 |
| 168 | [Project: Mini Version Control System (Like Git)](Day-168-Project-Mini-Version-Control-System-Like-Git/README.md) | 1 |
| 169 | [Project: Mini Search Engine (Inverted Index + TF-IDF)](Day-169-Project-Mini-Search-Engine-Inverted-Index-TF-IDF/README.md) | 1 |
| 170 | [Project: Password Manager (Encrypted Vault)](Day-170-Project-Password-Manager-Encrypted-Vault/README.md) | 1 |
| 171 | [Project: Task Scheduler and Reminder Service](Day-171-Project-Task-Scheduler-and-Reminder-Service/README.md) | 1 |
| 172 | [Project: Spam Classifier with Naive Bayes (ML from Scratch)](Day-172-Project-Spam-Classifier-with-Naive-Bayes-ML-from-Scratch/README.md) | 1 |
| 173 | [Project: Linear Regression from Scratch (Marks Predictor)](Day-173-Project-Linear-Regression-from-Scratch-Marks-Predictor/README.md) | 1 |
| 174 | [Project: K-Means Clustering from Scratch (Customer Segmentation)](Day-174-Project-K-Means-Clustering-from-Scratch-Customer-Segmentation/README.md) | 1 |
| 175 | [Project: Stock Portfolio Simulator](Day-175-Project-Stock-Portfolio-Simulator/README.md) | 1 |
| 176 | [Project: Micro-Grid Energy Management Simulator](Day-176-Project-Micro-Grid-Energy-Management-Simulator/README.md) | 1 |

---

Made with ❤️ by **Prasanna Kumar Pandey** · [github.com/prasanna6110](https://github.com/prasanna6110)

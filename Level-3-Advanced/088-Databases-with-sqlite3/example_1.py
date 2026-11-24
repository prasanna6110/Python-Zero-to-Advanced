# 088 · Databases with sqlite3 — Example 1: CRUD operations
# Run: python example_1.py

import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, branch TEXT, cgpa REAL)")
cur.executemany("INSERT INTO students (name, branch, cgpa) VALUES (?, ?, ?)",
                [("Asha", "EE", 9.1), ("Ravi", "CS", 8.4), ("Meera", "EE", 8.9)])
conn.commit()
cur.execute("UPDATE students SET cgpa = ? WHERE name = ?", (9.0, "Ravi"))
cur.execute("DELETE FROM students WHERE name = ?", ("Meera",))
for row in cur.execute("SELECT * FROM students ORDER BY cgpa DESC"):
    print(row)
conn.close()

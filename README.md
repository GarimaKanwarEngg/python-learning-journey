![Python](https://img.shields.io/badge/Python-3.14-blue)

# Python Learning Journey 🚀

Hi, I'm Garima 👩‍💻  
This repository contains my daily Python learning progress.

---

## 📅 Day 1 – Python Basics

### 📚 Topics Covered:
- print() function
- Checking Python version using `sys.version`
- Indentation in Python
- Variables (int & string)
- Comments (single line & multiline concept)
- Statements in Python
- Using semicolons
- `end` parameter in print()
- Printing numbers
- Mixing text and numbers in output

---

## 🧠 Key Learnings:

- Python uses indentation to define blocks of code.
- Variables can store different data types.
- Comments improve readability.
- `end` parameter controls line ending behavior.
- Semicolons are optional in Python.

---

## 📅Day 2: Python Variables & Data Types

**Today I learned about variables in Python and how to use them effectively.**

### Key Points
- Variables are containers for storing data values.
- Variables can change type dynamically.
- Use casting to set a specific data type.
- Variables are case-sensitive.
- Global vs Local variables.

### Example Code
x = 7
y = "Garima Kanwar"
print(x, y)

x = "Hello"  # changing type

x = str(3)
y = int(3)
z = float(3)
print(x, y, z)

# Global variable example
x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print(x)

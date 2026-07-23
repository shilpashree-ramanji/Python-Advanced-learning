# File Handling

## Definition

File Handling is the process of creating, reading, writing, updating, and managing files using Python. It allows programs to store data permanently instead of keeping it only in memory.

Python provides the built-in `open()` function to work with files.

---

## Why Do We Need It?

- Store data permanently.
- Read input data from files.
- Generate reports and logs.
- Process CSV, JSON, XML, and text files.
- Build ETL pipelines and data engineering applications.

---

## Example

```python
# Read a text file

with open("../../Input-Files/txt/sample.txt", "r") as file:
    content = file.read()
    print(content)
```

---

## Example Explanation

- `open()` opens the file.
- `"r"` opens the file in **Read** mode.
- `with open()` automatically closes the file after use.
- `read()` reads the complete contents of the file.
- `print()` displays the contents on the console.

---

## Common File Modes

| Mode | Description |
|------|-------------|
| `r` | Read an existing file |
| `w` | Write to a file (overwrites existing content) |
| `a` | Append data to the end of a file |
| `x` | Create a new file (fails if the file already exists) |

---

## Best Practice

Always use:

```python
with open("filename", "mode") as file:
    # File operations
```

instead of:

```python
file = open("filename", "mode")
# File operations
file.close()
```

because `with open()` automatically closes the file, even if an error occurs.
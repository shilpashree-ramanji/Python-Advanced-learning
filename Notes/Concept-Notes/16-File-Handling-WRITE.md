# Writing to a File

## Definition

Writing to a file is the process of storing data in a file using Python. If the file already exists, Python can overwrite its contents or create a new file if it doesn't exist.

Python uses the `write()` method to write data into a file.

---

## Why Do We Need It?

- Save user input permanently.
- Generate reports.
- Create log files.
- Store application data.
- Export processed data for ETL pipelines.

---

## Example

```python
with open("../../Input-Files/txt/output.txt", "w") as file:
    file.write("Hello Shilpa!\n")
    file.write("Welcome to Python File Handling.")
```

---

## Example Explanation

- `open()` opens the file.
- `"w"` opens the file in **Write** mode.
- If the file does not exist, Python creates it.
- If the file already exists, its previous contents are deleted.
- `write()` writes data into the file.
- `with open()` automatically closes the file after writing.

---

## Best Practice

Always use:

```python
with open("filename", "w") as file:
    file.write("Your data")
```

instead of manually opening and closing the file.

---

## Note

- `"w"` **overwrites** the existing file.
- Use `"a"` (Append mode) if you want to add data without deleting the existing contents.
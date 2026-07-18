# 📘 Class Variables

> **Level:** Beginner  
> **Category:** Object-Oriented Programming (OOP)  
> **Prerequisites:** Classes and Objects, Constructors, Instance Variables  
> **Hands-on File:** `Hands-on/04_class_variables.py`

---

# 📖 Definition / What is it?

A **class variable** is a variable that belongs to the **class itself**, rather than to individual objects.

Unlike instance variables, a class variable is **shared by all objects** created from the class.

It is declared directly inside the class, outside any methods.

---

# 🎯 Why do we need Class Variables?

Class variables help us:

- Store data common to all objects.
- Avoid duplicating the same value for every object.
- Reduce memory usage when the value is shared.
- Represent properties that belong to the class rather than a specific object.

---

# 📝 Syntax

```python
class ClassName:

    class_variable = value

    def __init__(self):
        pass
```

---

# 📚 Sub Topics

- Class Variables
- Accessing Class Variables
- Updating Class Variables
- Difference Between Class and Instance Variables

---

# 💻 Example Code

```python
class Student:

    school_name = "ABC Public School"

    def __init__(self, name):
        self.name = name


student1 = Student("Shilpa")
student2 = Student("Rahul")

print(student1.name, "-", student1.school_name)
print(student2.name, "-", student2.school_name)
```

---

# ✅ Code Output

```text
Shilpa - ABC Public School
Rahul - ABC Public School
```

---

# 🔍 Explain the Example

### Step 1

Create a class named `Student`.

```python
class Student:
```

---

### Step 2

Declare a class variable.

```python
school_name = "ABC Public School"
```

This variable belongs to the **Student** class.

Only one copy exists.

---

### Step 3

Create an instance variable.

```python
self.name = name
```

Each object gets its own `name`.

---

### Step 4

Create two objects.

```python
student1 = Student("Shilpa")
student2 = Student("Rahul")
```

Both objects share the same `school_name`.

---

### Step 5

Access the variables.

```python
print(student1.name, student1.school_name)
print(student2.name, student2.school_name)
```

Notice:

- `name` is different for each object.
- `school_name` is the same for all objects.

---

# 🌍 Real-World Analogy

Imagine a company.

Every employee has their own:

- Employee ID
- Name
- Salary

These are **instance variables**.

But all employees share:

- Company Name
- Company Address
- HR Email

These are **class variables**.

---

# ⭐ Key Points

- Class variables belong to the class.
- Only one copy exists.
- Shared by all objects.
- Declared outside methods.
- Accessed using either the class name or an object.

---

# 🎤 Interview Questions

### What is a class variable?

A class variable is a variable that belongs to the class and is shared by all objects.

---

### Where are class variables declared?

Inside the class but outside all methods.

---

### How do class variables differ from instance variables?

| Instance Variable | Class Variable |
|-------------------|----------------|
| Belongs to an object | Belongs to the class |
| Separate copy for each object | One shared copy |
| Created using `self` | Created directly in the class |

---

### How do you access a class variable?

Using either:

```python
Student.school_name
```

or

```python
student1.school_name
```

---

# 🚀 Data Engineering Connection

Class variables are useful for storing shared configuration such as:

- Environment Name
- Storage Account URL
- Database Port
- API Version
- Default File Format

Example:

```python
class AzureConfig:

    environment = "DEV"

    def __init__(self, storage_account):
        self.storage_account = storage_account
```

Every object has its own storage account, but all objects use the same environment.

---

# 📌 Summary

- Class variables belong to the class.
- They are shared by all objects.
- Only one copy exists.
- Declared outside methods.
- Useful for storing common information.

---

# ⏭️ Next Topic

➡️ **Instance Methods**
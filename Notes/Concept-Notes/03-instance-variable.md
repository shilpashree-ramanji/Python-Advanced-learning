# 📘 Instance Variables

> **Level:** Beginner  
> **Category:** Object-Oriented Programming (OOP)  
> **Prerequisites:** Classes and Objects, Constructors  
> **Hands-on File:** `Hands-on/03_instance_variables.py`

---

# 📖 Definition / What is it?

An **instance variable** is a variable that belongs to an **object (instance)** of a class.

Each object has its **own separate copy** of instance variables, which means changing the value in one object does **not** affect another object.

Instance variables are usually created inside the constructor (`__init__()`) using the `self` keyword.

---

# 🎯 Why do we need Instance Variables?

Instance variables help us:

- Store data specific to an object.
- Maintain the state of each object independently.
- Allow multiple objects of the same class to hold different values.
- Model real-world entities where every object has unique information.

---

# 📝 Syntax

```python
class ClassName:

    def __init__(self, parameter):
        self.variable_name = parameter
```

---

# 📚 Sub Topics

- Object State
- `self` Keyword
- Instance Variables
- Accessing Instance Variables

---

# 💻 Example Code

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Shilpa", 25)
student2 = Student("Rahul", 28)

print(student1.name, student1.age)
print(student2.name, student2.age)
```

---

# ✅ Code Output

```text
Shilpa 25
Rahul 28
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

Create the constructor.

```python
def __init__(self, name, age):
```

The constructor receives the values when an object is created.

---

### Step 3

Create instance variables.

```python
self.name = name
self.age = age
```

Here,

- `self.name` is an instance variable.
- `self.age` is an instance variable.

These variables belong to the object being created.

---

### Step 4

Create two objects.

```python
student1 = Student("Shilpa", 25)
student2 = Student("Rahul", 28)
```

Python creates two different objects.

Each object gets its own copy of:

- `name`
- `age`

---

### Step 5

Access the instance variables.

```python
print(student1.name, student1.age)
print(student2.name, student2.age)
```

Output:

```text
Shilpa 25
Rahul 28
```

Notice that each object stores different values even though both are created from the same class.

---

# 🌍 Real-World Analogy

Imagine a classroom.

Every student has their own:

- Name
- Age
- Roll Number
- Marks

Although all students belong to the same **Student** class, each student has different information.

Similarly, every object has its own instance variables.

---

# ⭐ Key Points

- Instance variables belong to an object.
- Every object has its own copy.
- They are usually initialized inside the constructor.
- They are accessed using the object name.
- Changes in one object's instance variables do not affect other objects.

---

# 🎤 Interview Questions

### What is an instance variable?

An instance variable is a variable that belongs to an object and stores data unique to that object.

---

### Where are instance variables created?

They are typically created inside the `__init__()` method using the `self` keyword.

---

### Can two objects have different values for the same instance variable?

Yes. Each object has its own copy of instance variables.

---

### How do you access an instance variable?

Using the object name.

Example:

```python
student.name
```

---

# 🚀 Data Engineering Connection

Instance variables are commonly used to store configuration specific to an object.

Examples include:

- Azure Storage Account Name
- Database Name
- Server Name
- API URL
- Container Name
- File Path

Example:

```python
class AzureStorage:

    def __init__(self, account_name, container):
        self.account_name = account_name
        self.container = container
```

Each `AzureStorage` object can connect to a different storage account or container by storing its own configuration.

---

# 📌 Summary

- Instance variables belong to an object.
- They store object-specific data.
- Every object has its own copy of instance variables.
- They are usually created using `self` inside the constructor.
- They help objects maintain their own state independently.

---

# ⏭️ Next Topic

➡️ **Class Variables**
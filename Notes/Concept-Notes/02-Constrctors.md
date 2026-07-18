# 📘 Constructors (`__init__`)

> **Level:** Beginner  
> **Category:** Object-Oriented Programming (OOP)  
> **Prerequisites:** Classes and Objects  
> **Estimated Reading Time:** 10–15 Minutes  
> **Hands-on File:** `Hands-on/02_constructors.py`

---

# 📖 Definition / What is it?

A **constructor** is a special method in Python that is **automatically executed when an object is created**.

In Python, the constructor is defined using the `__init__()` method.

Its primary purpose is to **initialize the object's attributes** with the values passed during object creation.

> **Note:** A constructor is called automatically—you don't call it explicitly.

---

# 🎯 Why do we need Constructors?

Without constructors, we would have to assign values to every object manually after creating it.

Constructors help us:

- Initialize object attributes automatically.
- Reduce repetitive code.
- Improve code readability.
- Create fully initialized objects.
- Make code easier to maintain.

---

# 📝 Syntax

```python
class ClassName:

    def __init__(self, parameter1, parameter2):
        self.parameter1 = parameter1
        self.parameter2 = parameter2


object_name = ClassName(value1, value2)
```

---

# 📚 Sub Topics

- `__init__()` Method
- `self` Keyword
- Parameters
- Instance Variables
- Default Constructors
- Parameterized Constructors

---

# 💻 Example Code

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Shilpa", 25)

print(student1.name)
print(student1.age)
```

---

# ✅ Code Output

```text
Shilpa
25
```

---

# 🔍 Explain the Example

### Step 1

Create a class.

```python
class Student:
```

---

### Step 2

Define the constructor.

```python
def __init__(self, name, age):
```

The constructor runs automatically whenever an object is created.

---

### Step 3

Initialize the object attributes.

```python
self.name = name
self.age = age
```

- `name` and `age` are parameters passed by the user.
- `self.name` and `self.age` become attributes of the object.

---

### Step 4

Create an object.

```python
student1 = Student("Shilpa", 25)
```

Python automatically calls:

```python
__init__("Shilpa", 25)
```

---

### Step 5

Access the attributes.

```python
print(student1.name)
print(student1.age)
```

The stored values are displayed.

---

# ⚙️ Constructor Execution Flow

```text
Create Object
      │
      ▼
__init__() is called automatically
      │
      ▼
Initialize object attributes
      │
      ▼
Object is ready to use
```

---

# 🌍 Real-World Analogy

Imagine buying a **new laptop**.

When you switch it on for the first time:

- Language is selected.
- Time zone is configured.
- Wi-Fi is connected.
- User account is created.

These setup steps happen before you start using the laptop.

Similarly, a constructor prepares an object before it is used.

---

# ⭐ Types of Constructors

## 1. Default Constructor

A constructor that doesn't require additional parameters.

```python
class Laptop:

    def __init__(self):
        print("Laptop Created")


lap = Laptop()
```

Output

```text
Laptop Created
```

---

## 2. Parameterized Constructor

A constructor that accepts values during object creation.

```python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


emp = Employee("Shilpa", 80000)
```

---

# ⭐ Key Points

- Constructor name must be `__init__()`.
- It executes automatically.
- Used to initialize object attributes.
- Every object can have different values.
- A constructor cannot return a value.
- `self` refers to the current object.

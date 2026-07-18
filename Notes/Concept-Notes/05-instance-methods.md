# 📘 Instance Methods

> **Level:** Beginner  
> **Category:** Object-Oriented Programming (OOP)  
> **Prerequisites:** Classes and Objects, Constructors, Instance Variables, Class Variables  
> **Hands-on File:** `Hands-on/05_instance_methods.py`

---

# 📖 Definition / What is it?

An **instance method** is a method that belongs to an object (instance) of a class.

It is defined inside a class and always takes **`self`** as its first parameter.

Instance methods can access and modify **instance variables** and **class variables**.

---

# 🎯 Why do we need Instance Methods?

Instance methods help us:

- Perform operations using object data.
- Access instance variables.
- Modify object state.
- Encapsulate behavior with data.
- Represent real-world actions.

---

# 📝 Syntax

```python
class ClassName:

    def __init__(self):
        pass

    def method_name(self):
        # Method body
```

---

# 📚 Sub Topics

- Instance Methods
- `self` Keyword
- Accessing Instance Variables
- Calling Instance Methods

---

# 💻 Example Code

```python
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_details(self):
        print("Name :", self.name)
        print("Marks:", self.marks)


student = Student("Shilpa", 95)

student.display_details()
```

---

# ✅ Code Output

```text
Name : Shilpa
Marks: 95
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

Initialize instance variables.

```python
self.name = name
self.marks = marks
```

---

### Step 3

Create an instance method.

```python
def display_details(self):
```

This method belongs to every object of the class.

---

### Step 4

Access instance variables.

```python
print(self.name)
print(self.marks)
```

The method accesses the current object's data using `self`.

---

### Step 5

Call the method.

```python
student.display_details()
```

Python automatically passes the object as `self`.

---

# 🌍 Real-World Analogy

Think of a **Car**.

The car has data:

- Brand
- Model
- Fuel Level

These are instance variables.

The car can also perform actions:

- Start
- Stop
- Accelerate

These actions are represented by instance methods.

---

# ⭐ Key Points

- Instance methods belong to objects.
- First parameter must be `self`.
- Can access instance variables.
- Can access class variables.
- Called using an object.

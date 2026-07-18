# 📘 Class Methods (`@classmethod`)

> **Level:** Intermediate  
> **Category:** Object-Oriented Programming (OOP)  
> **Prerequisites:** Instance Methods, Class Variables  
> **Hands-on File:** `Hands-on/06_class_methods.py`

---

# 📖 Definition / What is it?

A **class method** is a method that belongs to the **class** rather than an individual object.

It is defined using the `@classmethod` decorator and receives the **class (`cls`)** as its first parameter instead of `self`.

Class methods are commonly used to work with **class variables**.

---

# 🎯 Why do we need Class Methods?

Class methods help us:

- Access and modify class variables.
- Perform operations related to the class.
- Create alternative constructors.
- Avoid creating unnecessary objects.

---

# 📝 Syntax

```python
class ClassName:

    @classmethod
    def method_name(cls):
        # Method Body
```

---

# 📚 Sub Topics

- `@classmethod`
- `cls` Parameter
- Accessing Class Variables
- Modifying Class Variables

---

# 💻 Example Code

```python
class Student:

    school_name = "ABC Public School"

    @classmethod
    def display_school(cls):
        print("School:", cls.school_name)


Student.display_school()
```

---

# ✅ Code Output

```text
School: ABC Public School
```

---

# 🔍 Explain the Example

### Step 1

Create a class variable.

```python
school_name = "ABC Public School"
```

This variable belongs to the class.

---

### Step 2

Create a class method.

```python
@classmethod
def display_school(cls):
```

The `@classmethod` decorator tells Python that this method belongs to the class.

---

### Step 3

Use `cls` to access the class variable.

```python
print(cls.school_name)
```

`cls` represents the class itself.

---

### Step 4

Call the method.

```python
Student.display_school()
```

Unlike instance methods, no object is required.

---

# 🌍 Real-World Analogy

Imagine a company.

Every employee shares the same company name.

Instead of asking an employee for the company name, you ask the **company itself**.

A class method works in the same way—it interacts with information shared by the entire class.

---

# ⭐ Key Points

- Defined using `@classmethod`.
- First parameter is `cls`.
- Works with class variables.
- Can be called using the class name.
- Does not require an object.


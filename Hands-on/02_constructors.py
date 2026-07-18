"""
=========================================================
Topic 02 : Constructors (__init__)
File      : 02_constructors.py
Author    : Shilpa
=========================================================

Objective:
- Understand Constructors
- Learn how __init__() works
- Initialize object attributes
- Create multiple objects
- Use default parameter values

"""


# =========================================================
# Example 1 : Constructor with Parameters
# =========================================================

print("\n========== Example 1 : Constructor with Parameters ==========\n")

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Shilpashree", 28)

print("Name: ", student1.name)
print("Age: ", student1.age)

print("\n========== Example 2 : Multiple Objects ==========\n")

class Employee:

    def __init__(self,name,age,designation):
        self.name = name
        self.age = age
        self.designation = designation

employee1 = Employee("Shilpashree", 28, "Data Engineer")
employee2 = Employee("Jaggesh", 31, "Associate Consultant")
employee3 = Employee("Ajay", 29, "Manager")

print("Employee 1 name : ", employee1.name)
print("Employee 2 age: ", employee2.age)
print("Employee 3 designation : ", employee3.designation)


# =========================================================
# Example 3 : Constructor with Default Value
# =========================================================

print("\n========== Example 3 : Default Parameters ==========\n")

class Laptop:

    def __init__(self, Brand, RAM=16):
        self.Brand = Brand
        self.RAM = RAM

lap1 = Laptop("MacBook", 32)
lap2 = Laptop("Dell")

print(lap1.Brand , " RAM storage is : ", lap1.RAM)
print(lap2.Brand , " RAM Storage is : ", lap2.RAM)

# =========================================================
# Example 4 : Constructor Calling Another Method
# =========================================================

print("\n========== Example 4 : Calling Methods ==========\n")

class Mobiles:

    def __init__(self, Brand):
        self.Brand = Brand

    def display(self):
        print("Brand : ", self.Brand)

phone = Mobiles("Samsung")

phone.display()
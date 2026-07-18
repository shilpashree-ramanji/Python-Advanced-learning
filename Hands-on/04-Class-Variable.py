"""
=========================================================
Topic 04 : Class Variables
File      : 04_class_variables.py
Author    : Shilpa
=========================================================

Objective:
- Understand Class Variables
- Differentiate between Class and Instance Variables
- Access Class Variables
- Modify Class Variables
- Use Class Variables in Real-world Examples

"""


# =========================================================
# Example 1 : Basic Class Variable
# =========================================================

print("\n========== Example 1 : Basic Class Variable ==========\n")

class Student:

    School_name = "Infosys Intitute of Technology"  #Global or Class Variable

    def __init__(self, name):
        self.name = name                            # Instance variable


stu1 = Student("Shilpa")
stu2 = Student("Venkatesh")


print(stu1.name, "___", stu1.School_name)
print(stu1.name, "___", stu1.School_name)


# Accessing the class variable

print("College Name: ", Student.School_name)



# =========================================================
# Example 2 : Accessing Class Variable
# =========================================================

print("\n========== Example 2 : Accessing Class Variable ==========\n")


class Employee:

    company = "Infosys"

    def __init__(self, name):
        self.name = name


emp = Employee("Shilpa")

print("Using Object :", emp.company)
print("Using Class  :", Employee.company)


# =========================================================
# Example 3 : Updating Class Variable
# =========================================================

print("\n========== Example 3 : Updating Class Variable ==========\n")

class Car:
    
    wheel = 4

    def __init__(self, Brand):
        self.Brand = Brand


car1 = Car("BMW")
car2 = Car("AUDI")

print("\n BEFORE UPDATE\n")

print(car2.Brand ,"-->", car2.wheel)
print(car1.Brand ,"-->", car1.wheel)

Car.wheel = 8

print("\n AFTER UPDATE\n")
print(car2.Brand ,"-->", car2.wheel)
print(car1.Brand ,"-->", car1.wheel)



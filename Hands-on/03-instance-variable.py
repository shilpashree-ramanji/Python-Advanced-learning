"""
=========================================================
Topic 03 : Instance Variables
File      : 03_instance_variables.py
Author    : Shilpa
=========================================================

Objective:
- Understand Instance Variables
- Learn how each object stores its own data
- Access and modify instance variables
- Use instance variables in methods

"""


# =========================================================
# Example 1 : Basic Instance Variables
# =========================================================

print("\n========== Example 1 : Basic ==========\n")


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Shilpa", 25)

print("Name :", student1.name)
print("Age  :", student1.age)


# =========================================================
# Example 2 : Multiple Objects
# =========================================================

print("\n========== Example 2 : Multiple Objects ==========\n")


class Employee:

    def __init__(self, name, designation):
        self.name = name
        self.designation = designation


emp1 = Employee("Shilpa", "Data Engineer")
emp2 = Employee("Rahul", "Python Developer")

print(emp1.name, "-", emp1.designation)
print(emp2.name, "-", emp2.designation)


# =========================================================
# Example 3 : Updating Instance Variables
# =========================================================

print("\n========== Example 3 : Updating Values ==========\n")


class Laptop:

    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram


lap = Laptop("Dell", 8)

print("Before Update")
print(lap.brand, "-", lap.ram, "GB")

lap.ram = 16

print("\nAfter Update")
print(lap.brand, "-", lap.ram, "GB")


# =========================================================
# Example 4 : Using Instance Variables Inside Methods
# =========================================================

print("\n========== Example 4 : Methods ==========\n")


class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_details(self):
        print("Brand :", self.brand)
        print("Model :", self.model)


car = Car("Hyundai", "Creta")
car.display_details()


# =========================================================
# Example 5 : Data Engineering Example
# =========================================================

print("\n========== Example 5 : Data Engineering ==========\n")


class AzureStorage:

    def __init__(self, account_name, container):
        self.account_name = account_name
        self.container = container

    def connect(self):
        print(
            f"Connected to Storage Account '{self.account_name}'"
        )
        print(
            f"Container : {self.container}"
        )


storage = AzureStorage("mdfstorage", "landing")

storage.connect()


# =========================================================
# Example 6 : Each Object Has Its Own Data
# =========================================================

print("\n========== Example 6 : Independent Objects ==========\n")


class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance


acc1 = BankAccount("Shilpa", 5000)
acc2 = BankAccount("Rahul", 12000)

print(acc1.account_holder, "-", acc1.balance)
print(acc2.account_holder, "-", acc2.balance)

acc1.balance += 2000

print("\nAfter Depositing into Shilpa's Account")

print(acc1.account_holder, "-", acc1.balance)
print(acc2.account_holder, "-", acc2.balance)


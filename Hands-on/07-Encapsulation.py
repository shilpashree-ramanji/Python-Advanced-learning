"""
=========================================================
Topic 05 : Encapsulation
File      : 05_encapsulation.py
Author    : Shilpa
=========================================================

Objective:
- Understand Encapsulation
- Understand Public Variables
- Understand Protected Variables
- Understand Private Variables
- Access Private Variables using Methods
- Use Getter and Setter Methods
- Understand Encapsulation with Real-world Examples

"""


# =========================================================
# Example 1 : Public Variable
# =========================================================

print("\n========== Example 1 : Public Variable ==========\n")

class Student:

    def __init__(self, name):
        self.name = name  # Pubic variable

stu1 = Student("Shilpa")

print("Student Name: ", stu1.name)

# Public Variables can be accessed directly
stu1.name = "Shree"
print("Updated Name: ", stu1.name)


# =========================================================
# Example 2 : Protected Variable
# =========================================================

print("\n========== Example 2 : Protected Variable ==========\n")


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary   # Protected Variable

Emp1 = Employee("Shilpa", 15000)

print("Employee Name : ", Emp1.name)
print("Employee Salary : ", Emp1._salary)



# =========================================================
# Example 3 : Private Variable
# =========================================================

print("\n========== Example 3 : Private Variable ==========\n")


class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance


account1 = BankAccount("Shilpa", 150000000)
print("Account Holder : ", account1.account_holder)


# =========================================================
# Example 4 : Access Private Variable Using Getter
# =========================================================

print("\n========== Example 4 : Getter Method ==========\n")

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary
    
emp1 = Employee("Shilpa", 150000000)
print("Employee Name : ", emp1.name)

print("And Salary is : ", emp1.get_salary())


# =========================================================
# Example 5 : Modify Private Variable Using Setter
# =========================================================

print("\n========== Example 5 : Setter Method ==========\n")


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary
    
    def set_salary(self, new_salary):
        self.__salary = new_salary

emp1 = Employee("Shilpa", 15000000)

print("Before Updating Salary : ", emp1.get_salary())

emp1.set_salary(15230000)

print("After Setting the salary : ", emp1.get_salary())
"""
=========================================================
Topic 06 : Class Methods
File      : 06_class_methods.py
Author    : Shilpa
=========================================================

Objective:
- Understand Class Methods
- Learn @classmethod
- Understand the cls parameter
- Access and modify class variables
- Compare Instance Methods and Class Methods

"""


# =========================================================
# Example 1 : Basic Class Method
# =========================================================

print("\n========== Example 1 : Basic Class Method ==========\n")

class Student:

    school_name = "Infosys Institute of Technology"

    @classmethod
    def display_school(cls):
        print("School Name. : ", cls.school_name)


Student.display_school()


# =========================================================
# Example 2 : Accessing Class Variable
# =========================================================

print("\n========== Example 2 : Access Class Variable ==========\n")


class Employee:

    company_name = "Infosys Limited"

    @classmethod

    def company_details(cls):
        print("Company : ", cls.company_name)


Employee.company_details()


# =========================================================
# Example 3 : Updating Class Variable
# =========================================================

print("\n========== Example 3 : Update Class Variable ==========\n")

class Car:

    wheels = 4

    @classmethod
    def update_wheels(cls, new_wheels):
        cls.wheels = new_wheels

print("Before Updation: ", Car.wheels)

Car.wheels = 10

print("After Updatioon: ", Car.wheels)


# =========================================================
# Example 4 : Calling Class Method Using Object
# =========================================================

print("\n========== Example 4 : Using Object ==========\n")

class College:

    college_name = "BGSIT"

    @classmethod
    def display_college(cls):
        print("College: ", cls.college_name)


student1 = College()

student1.display_college()
"""
=========================================================
Topic 09 : Static Methods
File      : 09_static_method.py
Author    : Shilpa
=========================================================

Objective:
- Understand Static Methods
- Learn @staticmethod
- Difference between Instance, Class, and Static Methods
"""

print("\n========== Example 1 : Normal Method ==========\n")


class Calculator:

    def add(Self, a, b):
        return a + b

calc = Calculator()

print(calc.add(10,20))



print("\n========== Example 2 : Static Method ==========\n")


class Calculator:

    @staticmethod
    def add(a, b):
        return(a+b)


print(Calculator.add(11,11))

print("\n========== Example 3 : Calling Through Object ==========\n")


class Calculator:

    @staticmethod
    def multiply(a, b):
        return a * b


calc = Calculator()

print(calc.multiply(5, 6))


print("\n========== Example 4 : Utility Function ==========\n")


class temperatures:

    @staticmethod
    def cle_to_fah(celcius):
        return (celcius * 9/5) + 32

print(temperatures.cle_to_fah(25))


print("\n========== Example 5 : Validation ==========\n")


class Employee:

    @staticmethod
    def is_valid_age(age):
        return 18 <= age <= 60


print(Employee.is_valid_age(25))
print(Employee.is_valid_age(15))
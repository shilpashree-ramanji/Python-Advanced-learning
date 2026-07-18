"""
=========================================================
Topic 01 : Classes and Objects
File      : 01_classes_and_objects.py
Author    : Shilpa
=========================================================

Objective:
- Understand Classes
- Understand Objects
- Create Objects
- Call Methods
- Create Multiple Objects

"""
# =========================================================
# Example 1 : Creating a Simple Class
# =========================================================

print("\n========== Example 1 ==========\n")

class Student:

    def display(self):
        print("Welcome to Python OOPs..!!")

student1 = Student()
student1.display()


# =========================================================
# Example 2 : Multiple Objects
# =========================================================

print("\n========== Example 2 ==========\n")

class Car:
    def start(self):
        print("Car has started...!!!")

car1 = Car()
car2 = Car()

car1.start()


# =========================================================
# Example 3 : Different Classes
# =========================================================

print("\n========== Example 3 ==========\n")

class Dog:
    def bark(self):
        print("Woof Woof...!!!")

class Cat:
    def sound(self):
        print("Meow Meow..!!")

dog1 = Dog()
cat1 = Cat()

dog1.bark()
cat1.sound()

# =========================================================
# Example 4 : One Class - Multiple Methods
# =========================================================

print("\n========== Example 4 ==========\n")


class Calculator:

    def add(self):
        print("Addition")

    def subtract(self):
        print("Subtraction")

    def multiply(self):
        print("Multiplication")

    def divide(self):
        print("Division")

calc = Calculator()

calc.add()
calc.subtract()
calc.multiply()
calc.divide()


# =========================================================
# Example 8 : Creating Multiple Objects
# =========================================================

print("\n========== Example 5 ==========\n")

class Mobile:

    def calls(Self):
        print("Calling...!!")

iphone = Mobile()
samsung = Mobile()
Xiomi = Mobile()
OnePlus = Mobile()

iphone.calls()
samsung.calls()
Xiomi.calls()
OnePlus.calls()



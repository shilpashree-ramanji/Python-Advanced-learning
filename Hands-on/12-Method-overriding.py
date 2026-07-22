"""
=========================================================
Topic 10 : Method Overriding
File      : 10_method_overriding.py
Author    : Shilpa
=========================================================

Objective:
- Understand Method Overriding
- Learn how child classes override parent methods
- Understand Runtime Polymorphism
"""

print("\n========== Example 1 : Basic Overriding ==========\n")

class Animal:

    def sound(self):
        print("Animals makes sound")



class Dog(Animal):

    def sound(Self):
        print("Dog makes woof woof sound")


dog = Dog()
dog.sound()


print("\n========== Example 2 : Parent Object ==========\n")


class Animal:

    def sound(self):
        print("Animals make sounds")


animal = Animal()
animal.sound()


print("\n========== Example 3 : super() ==========\n")


class Animal:

    def sound(self):
        print("Animals makes sound")

class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog Says Woof Woof")

dog = Dog()
dog.sound()
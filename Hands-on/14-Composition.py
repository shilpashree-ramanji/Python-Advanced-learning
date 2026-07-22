"""
=========================================================
Topic 13 : Composition
File      : 13_composition.py
Author    : Shilpa
=========================================================

Objective:
- Understand Composition
- Learn Has-A Relationship
- Compare Composition and Inheritance
"""

print("\n========== Example 1 ==========\n")


class Engine:

    def start(self):
        print("Engine Started")


class Car:

    def __init__(self):
        self.engine = Engine()

    def drive(self):
        print("Car is Ready")
        self.engine.start()


car = Car()

car.drive()

print("\n========== Example 2 ==========\n")


class Keyboard:

    def type(self):
        print("Typing...")


class Laptop:

    def __init__(self):
        self.keyboard = Keyboard()

    def work(self):
        print("Laptop Started")
        self.keyboard.type()


laptop = Laptop()

laptop.work()
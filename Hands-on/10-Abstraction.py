"""
=========================================================
Topic 08 : Abstraction
File      : 08_abstraction.py
Author    : Shilpa
=========================================================

Objective:
- Understand Abstraction
- Learn Abstract Classes
- Learn Abstract Methods
- Implement Abstraction using abc module
- Understand Real-world Examples

"""

from abc import ABC, abstractmethod

# =========================================================
# Example 1 : Abstract Class
# =========================================================

print("\n========== Example 1 : Abstract Class ==========\n")


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog says Wooff")


dog = Dog()
dog.sound()

print("\n========== Example 2 : Multiple Child Classes ==========\n")

class Shape(ABC):

    @abstractmethod
    def Area(self):
        print("Hehe Done")

class Circle(Shape):
    
    def Area(self):
        print("Area of Circle")

class Rectangle(Shape):

    def Area(self):
        print("Area of Rectangle")


circ = Circle()
rect = Rectangle()

circ.Area()
rect.Area()
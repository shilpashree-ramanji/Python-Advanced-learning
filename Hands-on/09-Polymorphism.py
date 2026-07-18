"""
=========================================================
Topic 07 : Polymorphism
File      : 07_polymorphism.py
Author    : Shilpa
=========================================================

Objective:
- Understand Polymorphism
- Understand Method Overriding
- Understand Runtime Polymorphism
- Understand Duck Typing
- Use Built-in Polymorphism
- Implement Real-world Examples

"""


# =========================================================
# Example 1 : Basic Polymorphism
# =========================================================

print("\n========== Example 1 : Basic Polymorphism ==========\n")

class Dog:
    def sound(self):
        print("Dog say woog...!!!")

class Cat:
    def sound(self):
        print("Cat say meow...!!!")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()



# =========================================================
# Example 2 : Method Overriding
# =========================================================

print("\n========== Example 2 : Method Overriding ==========\n")



class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog says Woof")


dog = Dog()

dog.sound()

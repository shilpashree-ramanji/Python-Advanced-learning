01. Classes and Objects
1. Definition / What is it?
Class

A class is a blueprint or template used to create objects. It defines the properties (attributes) and behaviors (methods) that objects created from the class will have.

Object

An object is an instance of a class. It is a real-world entity created from the blueprint (class) and contains its own data.

2. Why do we need it?

Without classes, managing related data and functions becomes difficult as applications grow.

Classes and objects help us to:

Organize code in a structured way.
Reuse code efficiently.
Represent real-world entities in software.
Improve readability and maintainability.
Build scalable applications.
3. Syntax
class ClassName:
    # Attributes
    # Methods

# Creating an object
object_name = ClassName()
4. Sub Topics
Class
Object
Attributes
Methods
Constructor (__init__) (covered in the next topic)
5. Example Code
class Student:

    def display(self):
        print("Welcome to Python OOP!")

student1 = Student()

student1.display()
6. Code Output
Welcome to Python OOP!
7. Explain the Example
Step 1
class Student:

A class named Student is created.

Step 2
def display(self):

A method named display() is defined inside the class.

The self parameter represents the current object calling the method.

Step 3
student1 = Student()

An object named student1 is created from the Student class.

Step 4
student1.display()

The object calls the display() method, which prints:

Welcome to Python OOP!
8. Real-World Analogy

Imagine a car showroom.

Class

The design or blueprint used to manufacture cars.

Objects

Individual cars produced using that blueprint.

Example:

Car 1 → Red
Car 2 → Blue
Car 3 → Black

All these cars are different objects created from the same class.

9. Key Points
A class is a blueprint.
An object is an instance of a class.
One class can create multiple objects.
Objects have their own data.
Methods define the behavior of objects.
Every object belongs to a class.
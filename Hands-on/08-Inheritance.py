"""
=========================================================
Topic 06 : Inheritance
File      : 06_inheritance.py
Author    : Shilpa
=========================================================

Objective:
- Understand Inheritance
- Understand Parent and Child Classes
- Inherit Methods from Parent Class
- Understand Single Inheritance
- Understand Multilevel Inheritance
- Understand Multiple Inheritance
- Understand Hierarchical Inheritance
- Use super() with Inheritance
- Understand Method Overriding

"""


# =========================================================
# Example 1 : Basic Inheritance
# =========================================================

print("\n========== Example 1 : Basic Inheritance ==========\n")


class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog1 = Dog()

# Method inherited from Parent class
dog1.eat()

# Method from Child class
dog1.bark()



# =========================================================
# Example 2 : Single Inheritance
# =========================================================

print("\n========== Example 2 : Single Inheritance ==========\n")


class Parents:

    def parent_method(self):
        print("This is Parent class")


class Children(Parents):

    def child_method(self):
        print("This is child Class")


child1 = Children()

child1.parent_method()
child1.child_method()


# =========================================================
# Example 3 : Inheriting Variables and Methods
# =========================================================

print("\n========== Example 3 : Inheriting Variables and Methods ==========\n")


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_employee(self):
        print("Name : ", self.name)
        print("Salary : ", self.salary)

class developer(Employee):

    def show_roles(self):
        print("Rols is : Developer")


dev1 = developer("Shilpa", 1500000)

dev1.display_employee()
dev1.show_roles()



# =========================================================
# Example 4 : Using super()
# =========================================================

print("\n========== Example 4 : Using super() ==========\n")


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class develope(Employee):

    def __init__(self, name, salary, langauge):
        #  Call Parent class constructor
        super().__init__(name, salary)
        self.langauge = langauge

    def display_details(self):
        print("Name is :", self.name)
        print("Salary is : ", self.salary)
        print("langauge : ", self.langauge)

dev1 = develope("Shilpa", 15000000, "Pyhton")
dev1.display_details()



# =========================================================
# Example 5 : Method Overriding
# =========================================================

print("\n========== Example 5 : Method Overriding ==========\n")


class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog says Woof")


dog1 = Dog()

dog1.sound()



# =========================================================
# Example 6 : Multilevel Inheritance
# =========================================================

print("\n========== Example 6 : Multilevel Inheritance ==========\n")

class GrandParent:
    def grandparent_method(self):
        print("This is GrandParent Method")

class Parent(GrandParent):
    def parent_method(self):
        print("This is Parent Method")

class Child(Parent):
    def child_method(self):
        print("This is called child method")

child1 = Child()
child1.grandparent_method()
child1.parent_method()
child1.child_method()



# =========================================================
# Example 7 : Multiple Inheritance
# =========================================================

print("\n========== Example 7 : Multiple Inheritance ==========\n")

class Father:
    def father_skills(self):
        print("Father knows cooking")

class Mother:
    def mother_skills(self):
        print("Mother knows everything")

class Child(Father, Mother):
    def child_skills(self):
        print("Child knows cooking")

child1 = Child()

child1.father_skills()
child1.mother_skills()
child1.child_skills()



# =========================================================
# Example 8 : Hierarchical Inheritance
# =========================================================

print("\n========== Example 8 : Hierarchical Inheritance ==========\n")


class Employee:
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def code(self):
        print("Developer is coding")

class Tester(Employee):
    def test(self):
        print("Tester is testing")

dev1 = Developer()
test1 = Tester()

dev1.work()
dev1.code()

test1.work()
test1.test()
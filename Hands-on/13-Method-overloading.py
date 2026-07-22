"""
=========================================================
Topic 12 : Method Overloading
File      : 12_method_overloading.py
Author    : Shilpa
=========================================================

Objective:
- Understand Method Overloading
- Learn why Python doesn't support it
- Learn alternatives using Default Arguments and *args
"""

print("\n========== Example 1 ==========\n")

class Claculator:

    def add(self, a, b):
        print(a + b)

    def add(self, a, b, c):
        print(a+b+c)

calc1 = Claculator()

#calc1.add(1,2)
calc1.add(1,2,3)

print("\n========== Example 2 ==========\n")


class Calculator:

    def add(self, a, b, c=0):
        print(a + b + c)


calc = Calculator()

calc.add(10, 20)

calc.add(10, 20, 30)


print("\n========== Example 3 ==========\n")


class Calculator:

    def add(self, *numbers):
        print(sum(numbers))


calc = Calculator()

calc.add(10, 20)

calc.add(10, 20, 30)

calc.add(10, 20, 30, 40)
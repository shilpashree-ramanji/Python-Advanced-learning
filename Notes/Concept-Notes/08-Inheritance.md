# Inheritance

## Definition

Inheritance is one of the four pillars of Object-Oriented Programming (OOP).

It allows a **child class** to inherit the properties (variables) and behaviors (methods) of an existing **parent class**. This promotes **code reusability** by allowing us to reuse existing code instead of writing it again.

---

## Why Do We Need Inheritance?

* To reuse existing code.
* To reduce code duplication.
* To make code easier to maintain.
* To establish a parent-child relationship between classes.
* To extend existing functionality without modifying the parent class.

---

## Example

```python
class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog1 = Dog()

dog1.eat()
dog1.bark()
```

### Output

```text
Animal is eating
Dog is barking
```

---

## Example Explanation

* `Animal` is the **Parent (Base) Class**.
* `Dog` is the **Child (Derived) Class**.
* `Dog` inherits the `eat()` method from the `Animal` class.
* `Dog` also has its own method `bark()`.
* Since `Dog` inherits from `Animal`, it can use both the inherited method (`eat()`) and its own method (`bark()`).

This is **Inheritance** because the child class (`Dog`) reuses the properties and methods of the parent class (`Animal`) without rewriting them.

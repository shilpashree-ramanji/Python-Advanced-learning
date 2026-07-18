# Polymorphism

## Definition

Polymorphism is one of the four pillars of Object-Oriented Programming (OOP).

The word **Polymorphism** means **"Many Forms."**

It allows the **same method name** to perform **different actions** depending on the object that calls it.

---

## Why Do We Need Polymorphism?

* To write flexible and reusable code.
* To use the same interface for different objects.
* To improve code readability and maintainability.
* To make programs easier to extend without changing existing code.
* To support runtime method selection.

---

## Example

```python
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog says Woof")


class Cat(Animal):

    def sound(self):
        print("Cat says Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
```

### Output

```text
Dog says Woof
Cat says Meow
```

---

## Example Explanation

* `Animal` is the parent class.
* `Dog` and `Cat` are child classes.
* Both child classes **override** the `sound()` method of the parent class.
* The method name remains the same (`sound()`), but the behavior changes based on the object calling it.
* When `dog.sound()` is called, it prints **"Dog says Woof"**.
* When `cat.sound()` is called, it prints **"Cat says Meow"**.

This is **Polymorphism** because the **same method** (`sound()`) has **different implementations** for different objects.

# Method Overriding

## Definition

Method Overriding is an Object-Oriented Programming (OOP) feature where a **child class provides its own implementation of a method that already exists in the parent class**.

The child class overrides the parent's method while keeping the same method name and parameters.

---

## Why Do We Need Method Overriding?

- To customize the behavior of inherited methods.
- To provide child-specific implementation.
- To achieve Runtime Polymorphism.
- To improve flexibility and code reusability.

---

## Example

```python
class Animal:

    def sound(self):
        print("Animals make sounds")


class Dog(Animal):

    def sound(self):
        print("Dog says Woof")


dog = Dog()
dog.sound()
```

### Output

```text
Dog says Woof
```

---

## Example Explanation

- `Animal` is the parent class with the `sound()` method.
- `Dog` inherits from `Animal`.
- The `Dog` class overrides the `sound()` method by providing its own implementation.
- When `dog.sound()` is called, Python executes the `Dog` class method instead of the `Animal` class method.

This is called **Method Overriding** because the child class replaces the behavior of the parent class method.
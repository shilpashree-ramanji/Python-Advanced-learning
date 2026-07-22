# Composition

## Definition

Composition is an Object-Oriented Programming (OOP) concept where one class contains an object of another class.

It represents a **Has-A Relationship**, allowing one class to use the functionality of another class without inheriting from it.

---

## Why Do We Need Composition?

- To achieve code reuse without inheritance.
- To build flexible and modular applications.
- To reduce tight coupling between classes.
- To model real-world **Has-A** relationships.

---

## Example

```python
class Engine:

    def start(self):
        print("Engine Started")


class Car:

    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()


car = Car()
car.drive()
```

### Output

```text
Engine Started
```

---

## Example Explanation

- `Car` contains an object of the `Engine` class.
- `Car` does not inherit from `Engine`.
- The `Car` object uses the `Engine` object to start the engine.
- This represents a **Has-A Relationship** because a car has an engine.

This is called **Composition**.
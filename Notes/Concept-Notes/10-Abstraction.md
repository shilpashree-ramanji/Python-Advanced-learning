# Abstraction

## Definition

Abstraction is one of the four pillars of Object-Oriented Programming (OOP).

It means **hiding the implementation details and showing only the essential functionality to the user**.

In Python, abstraction is implemented using **Abstract Classes** and **Abstract Methods** from the `abc` module.

---

## Why Do We Need Abstraction?

- To hide complex implementation details.
- To expose only the required functionality to the user.
- To improve code readability and maintainability.
- To enforce a common structure for child classes.
- To reduce code complexity.

---

## Example

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


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

- `Animal` is an **Abstract Class**.
- `sound()` is an **Abstract Method**.
- The `Dog` class inherits from `Animal`.
- Since `Dog` inherits from an abstract class, it **must implement** the `sound()` method.
- When `dog.sound()` is called, the implementation in the `Dog` class is executed.
- The user only knows that `sound()` can be called, while the implementation is provided by the child class.

This is **Abstraction** because the abstract class defines **what should be done**, while the child class defines **how it should be done**.
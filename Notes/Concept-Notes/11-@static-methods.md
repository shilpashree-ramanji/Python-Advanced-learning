# Static Method

## Definition

A **Static Method** is a method that belongs to a class but **does not use instance data (`self`) or class data (`cls`)**.

It is created using the `@staticmethod` decorator and is mainly used for utility or helper functions related to the class.

---

## Why Do We Need Static Methods?

- To perform operations that do not depend on object or class data.
- To group utility functions inside a class.
- To improve code organization and readability.
- To call methods without creating an object.

---

## Example

```python
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


result = Calculator.add(10, 20)

print(result)
```

### Output

```text
30
```

---

## Example Explanation

- `add()` is a **Static Method** because it does not use `self` or `cls`.
- It simply adds two numbers.
- The method is called using the class name (`Calculator.add()`), so no object creation is required.
- Static methods are useful for utility functions that are related to a class but do not depend on its data.
# Method Overloading

## Definition

Method Overloading is an Object-Oriented Programming (OOP) concept where multiple methods have the **same name** but **different parameters**.

Python **does not support traditional Method Overloading**. Instead, similar behavior can be achieved using **default arguments** or **`*args`**.

---

## Why Do We Need Method Overloading?

- To perform the same operation with different numbers of inputs.
- To make methods more flexible.
- To reduce the need for multiple method names.
- In Python, this is achieved using **default arguments** or **`*args`**.

---

## Example

```python
class Calculator:

    def add(self, *numbers):
        return sum(numbers)


calc = Calculator()

print(calc.add(10, 20))
print(calc.add(10, 20, 30))
```

### Output

```text
30
60
```

---

## Example Explanation

- `add()` accepts any number of arguments using `*numbers`.
- The `sum()` function adds all the numbers passed to the method.
- The same method can handle different numbers of inputs without creating multiple methods.

This is Python's way of achieving behavior similar to **Method Overloading**.
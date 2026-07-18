# Encapsulation

## Definition

Encapsulation is one of the four pillars of Object-Oriented Programming (OOP).

It means **bundling data (variables) and methods together inside a class and controlling how the data is accessed or modified**.

Encapsulation helps protect an object's internal data from unwanted or accidental changes.

---

## Why Do We Need Encapsulation?

* To protect internal data.
* To control how data is accessed and modified.
* To prevent accidental changes to data.
* To add validation before updating data.
* To improve code security and maintainability.

---

## Example

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount


account1 = BankAccount(10000)

print(account1.get_balance())

account1.deposit(5000)

print(account1.get_balance())
```

### Output

```text
10000
15000
```

---

## Example Explanation

* `__balance` is a **private variable**.
* The balance is stored inside the `BankAccount` class.
* `get_balance()` is used to access the balance.
* `deposit()` is used to modify the balance in a controlled way.
* The `deposit()` method checks that the amount is greater than `0` before updating the balance.
* This prevents invalid values from being added to the account.

This is **Encapsulation** because the data (`__balance`) and the methods that operate on it (`get_balance()` and `deposit()`) are bundled together, while access to the data is controlled.

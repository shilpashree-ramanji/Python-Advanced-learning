"""
=========================================================
Topic : Iterators
File  : iterator.py
Author: Shilpa
=========================================================

Objective:
- Understand Iterators
- Understand iter()
- Understand next()
- Understand StopIteration
- Understand how for loops use iterators
"""


# =========================================================
# Example 1 : Basic Iterator
# =========================================================

print("\n========== Example 1 : Basic Iterator ==========\n")

numbers = [10,20,30,40,50]

iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        break


print("\n========== Example 5 : String Iterator ==========\n")

name = "Python"

iterator = iter(name)

print(next(iterator))
print(next(iterator))
print(next(iterator))
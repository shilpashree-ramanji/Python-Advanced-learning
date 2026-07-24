# Iterators

## Definition

An **Iterator** is an object that returns elements **one at a time**.

Python uses:

- `iter()` → Creates an iterator from an iterable.
- `next()` → Returns the next element from the iterator.
- `StopIteration` → Raised when there are no more elements.

---

## Why Do We Need Iterators?

- To access elements one at a time.
- To avoid manually managing indexes.
- To work efficiently with sequences of data.
- Python `for` loops internally use iterators.
- They form the foundation for understanding **Generators** and lazy processing.

---

## Example

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

### Output

```text
10
20
30
```

---

## Example Explanation

- `numbers` is an **Iterable** because we can loop through it.
- `iter(numbers)` creates an **Iterator**.
- `next(iterator)` returns one value at a time.
- Each `next()` call moves to the next element.
- When there are no elements remaining, Python raises `StopIteration`.

The basic flow is:

```text
Iterable
   ↓
 iter()
   ↓
Iterator
   ↓
 next()
   ↓
One value at a time
```

---

## Iterable vs Iterator

| Iterable | Iterator |
|---|---|
| Contains data that can be looped over | Returns values one at a time |
| Examples: List, Tuple, String, Set | Created using `iter()` |
| Used with `iter()` | Used with `next()` |

---

## Important to Remember

A Python `for` loop internally uses the Iterator mechanism:

```text
iter() → next() → next() → next() → StopIteration
```

When `StopIteration` occurs, the `for` loop automatically stops.
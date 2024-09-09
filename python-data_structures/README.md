
# Python - Data Structures: Lists, Tuples

## Description
In this section, we explore two essential data structures in Python: **Lists** and **Tuples**. These data structures allow us to store multiple elements and provide various methods to manipulate them. We will learn how to create, modify, and iterate over lists and tuples, and how to use Python's built-in functions to work efficiently with these structures.

## Learning Objectives
By the end of this section, you will be able to:
- Understand the difference between lists and tuples.
- Create lists and tuples in Python.
- Perform operations such as adding, removing, and updating elements in a list.
- Access elements in lists and tuples using indexing and slicing.
- Use built-in functions and methods such as `len()`, `append()`, `remove()`, `index()`, and others.
- Understand how to loop through lists and tuples using `for` and `while` loops.
- Work with list comprehensions to create and manipulate lists.
- Understand immutability in tuples and how it differs from lists.
- Perform common operations on tuples like concatenation and unpacking.

## Key Concepts

### Lists
- Lists are mutable, meaning you can change, add, or remove elements after the list is created.
- Lists are ordered, so elements have a defined order, and you can access elements by their index.

### Tuples
- Tuples are immutable, meaning once they are created, their elements cannot be changed.
- Like lists, tuples are ordered, and you can access elements by their index.

## Example Code

### Creating a List
```python
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]
```

### Creating a Tuple
```python
my_tuple = (10, 20, 30)
print(my_tuple)  # Output: (10, 20, 30)
```

### Modifying a List
```python
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]
```

### Accessing Elements by Index
```python
print(my_list[0])  # Output: 1
print(my_tuple[1])  # Output: 20
```

### Looping Through Lists
```python
for item in my_list:
    print(item)
```

### List Comprehension
```python
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]
```

## Additional Resources
- [Python Documentation - Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Python Documentation - Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

## Author
[Irina Mora (IrenBod)]

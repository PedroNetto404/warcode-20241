# Python Data Structures Guide

This guide provides a brief overview of the main data structures available in Python, including examples of how to use them.

## 1. Lists
A list in Python is an ordered collection of items which can be of any type. Lists are mutable, meaning you can change their content.

```python
# Creating a list
my_list = [1, 2, 3]
print(my_list)

# Adding elements
my_list.append(4)
print(my_list)

# Accessing elements
print(my_list[0])  # Output: 1
```

## 2. Tuples
A tuple in Python is similar to a list except that it is immutable. Once a tuple is created, its content cannot be changed.

```python
# Creating a tuple
my_tuple = (1, 2, 3)
print(my_tuple)

# Accessing elements
print(my_tuple[1])  # Output: 2
```

## 3. Dictionaries
A dictionary in Python is an unordered collection of data values, used to store data values like a map.

```python
# Creating a dictionary
my_dict = {'name': 'John', 'age': 30}
print(my_dict)

# Accessing elements
print(my_dict['name'])  # Output: John
```

## 4. Sets
A set is an unordered collection of unique elements. Sets are mutable and can be used to perform mathematical set operations.

```python
# Creating a set
my_set = {1, 2, 3}
print(my_set)

# Adding elements
my_set.add(4)
print(my_set)
```

### Conclusion
These are the basic data structures in Python that are commonly used for a variety of programming tasks.

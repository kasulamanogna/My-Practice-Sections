'''
# Module 3: Data Structures Assignments
## Lesson 3.4: Dictionaries
### Assignment 1: Creating and Accessing Dictionaries

Create a dictionary with the first 10 positive integers as keys and their squares as values. Print the dictionary.

### Assignment 2: Accessing Dictionary Elements

Print the value of the key 5 and the keys of the dictionary created in Assignment 1.

### Assignment 3: Dictionary Methods

Add a new key-value pair (11, 121) to the dictionary created in Assignment 1 and then remove the key-value pair with key 1. Print the modified dictionary.

### Assignment 4: Iterating Over Dictionaries

Iterate over the dictionary created in Assignment 1 and print each key-value pair.

### Assignment 5: Dictionary Comprehensions

Create a new dictionary containing the cubes of the first 10 positive integers using a dictionary comprehension. Print the new dictionary.

### Assignment 6: Merging Dictionaries

Create two dictionaries: one with keys as the first 5 positive integers and values as their squares, and another with keys as the next 5 positive integers and values as their squares. Merge these dictionaries into a single dictionary and print it.

### Assignment 7: Nested Dictionaries

Create a nested dictionary representing a student with keys 'name', 'age', 'grades', where 'grades' is another dictionary with keys 'math', 'science', and 'english'. Print the nested dictionary.

### Assignment 8: Dictionary of Lists

Create a dictionary where the keys are the first 5 positive integers and the values are lists containing the first 5 multiples of the key. Print the dictionary.

### Assignment 9: Dictionary of Tuples

Create a dictionary where the keys are the first 5 positive integers and the values are tuples containing the key and its square. Print the dictionary.

### Assignment 10: Dictionary and List Conversion

Create a dictionary with the first 5 positive integers as keys and their squares as values. Convert the dictionary to a list of tuples and print it.

### Assignment 11: Dictionary Filtering

Create a dictionary with the first 10 positive integers as keys and their squares as values. Create a new dictionary containing only the key-value pairs where the key is even. Print the new dictionary.

### Assignment 12: Dictionary Key and Value Transformation

Create a dictionary with the first 5 positive integers as keys and their squares as values. Create a new dictionary with keys and values swapped. Print the new dictionary.

### Assignment 13: Default Dictionary

Create a default dictionary where each key has a default value of an empty list. Add some elements to the lists and print the dictionary.

### Assignment 14: Counting with Dictionaries

Write a function that takes a string and returns a dictionary with the count of each character in the string. Print the dictionary.

### Assignment 15: Dictionary and JSON

Create a dictionary representing a book with keys 'title', 'author', 'year', and 'genre'. Convert the dictionary to a JSON string and print it.

'''

# Assignment 1
d = {i: i**2 for i in range(1, 11)}
print(d)

# Assignment 2

print(d[5])
print(d.keys())

# Assignment 3
d[11] = 121
d.pop(1)
print(d)

# Assignment 4
for key, value in d.items():
    print(f"{key} : {value}")

# Assignment 5
i = {i: i**3 for i in range(1, 11)}
print(i)

# Assignment 6

merging_d1 = {i: i**2 for i in range(1, 6)}
merging_d2 = {i: i**2 for i in range(6, 11)}

merging_d1.update(merging_d2)
print(merging_d1)

# Assignment 7
nested_dict = {
    "name":"manu",
    "age":24,
    "greads":{
        "math":89,
        "science":90,
        "social":60
    }

}
print(nested_dict)

# Assignment 8
multiples = {i: [i * j for j in range(1, 6)]for i in range(1, 6)}
print(multiples)

# Assignment 9
dict_tpl = {i: (i, i**2) for i in range(1, 6)}
print(dict_tpl)

# Assignment 10
dict = {i: 1**2 for i in range(1, 6)}
convert_to_list = list(dict.items())
print(convert_to_list)

# Assignment 11
d = {i: i**2 for i in range(1, 6)}
values_keys = {k: v for k, v in d.items() if k % 2 == 0}
print(values_keys)

# Assignment 12
d = {i: i**2 for i in range(1, 6)}
swap = {v: k for k, v in d.items()}
print(swap)

# Assignment 13
from collections import defaultdict

default_dict = defaultdict(list)
default_dict['a'].append(1)
default_dict['a'].append(2)
default_dict['b'].append(4)
default_dict['c'].append(5)
print(default_dict)


# Assignment 14
def count_chars(s):
    count_dict = {}
    for char in s:
        count_dict[char] = count_dict.get(char, 0) + 1
    return count_dict

string = "hello world"
print(count_chars(string))

# Assignment 15
import json

book = {
    'title': 'To Kill a Mockingbird',
    'author': 'Harper Lee',
    'year': 1960,
    'genre': 'Fiction'
}
book_json = json.dumps(book)
print(book_json)


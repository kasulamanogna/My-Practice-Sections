'''
# Module 3: Data Structures Assignments
## Lesson 3.3: Sets
### Assignment 1: Creating and Accessing Sets

Create a set with the first 10 positive integers. Print the set.

### Assignment 2: Adding and Removing Elements

Add the number 11 to the set created in Assignment 1. Then remove the number 1 from the set. Print the modified set.

### Assignment 3: Set Operations

Create two sets: one with the first 5 positive integers and another with the first 5 even integers. Perform and print the results of union, intersection, difference, and symmetric difference operations on these sets.

### Assignment 4: Set Comprehensions

Create a new set containing the squares of the first 10 positive integers using a set comprehension. Print the new set.

### Assignment 5: Filtering Sets

Create a new set containing only the even numbers from the set created in Assignment 1 using a set comprehension. Print the new set.

### Assignment 6: Set Methods

Create a set with duplicate elements and remove the duplicates using set methods. Print the modified set.

### Assignment 7: Subsets and Supersets

Create two sets: one with the first 5 positive integers and another with the first 3 positive integers. Check if the second set is a subset of the first set and if the first set is a superset of the second set. Print the results.

### Assignment 8: Frozenset

Create a frozenset with the first 5 positive integers. Print the frozenset.

### Assignment 9: Set and List Conversion

Create a set with the first 5 positive integers. Convert it to a list, append the number 6, and convert it back to a set. Print the resulting set.

### Assignment 10: Set and Dictionary

Create a dictionary with set keys and integer values. Print the dictionary.

'''

# Assignment 1

a = {1,2,3,4,5,6,7,8,9,10}
print(a)

a = set(range(1, 11))
print(a)

# Assignment 2
a.add(11)
print(a)
a.remove(1)
print(a)

# Assignment 3
set1 = set(range(1, 6))
set2 = set(range(2, 11, 2))
print(set1)
print(set2)

print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")
print(f"Symmantric difference: {set1 ^ set2}")


# Assignment 4

squres = {x**2 for x in range(1, 11)}
print(squres)

# Assignment 5
evens = {x for x in range(1, 11) if x%2 == 0}
print(evens)

# Assignments 6
creat_set = {1,2,2,3,4,5,6,7,7,7,7,8,89}
unique_set = set(creat_set)
print(unique_set)

# Assignment 7

set1 = set(range(1, 6))
set2 = set(range(1, 4))
print(set1)
print(set2)

print(f"Subset: {set2.issubset(set1)}")
print(f"superset: {set1.issuperset(set2)}")

# Assignment 8
fs = frozenset(range(1, 11))
print(fs)

# Assignment 9
c_s = set(range(1, 6))
convert_to_list = list(c_s)
print(convert_to_list)
convert_to_list.append(6)
convert_to_set = set(convert_to_list)
print(convert_to_set) 

# Assignment 10
dict = {
    frozenset({1, 2}):3,
    frozenset({4, 5}):6,
    frozenset({7, 8}):9
}
print(dict)


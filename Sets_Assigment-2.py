'''### Assignment 11: Iterating Over Sets

Create a set and iterate over the elements, printing each element.

### Assignment 12: Removing Elements from Sets

Create a set and remove elements from it until it is empty. Print the set after each removal.

### Assignment 13: Set Symmetric Difference Update

Create two sets and update the first set with the symmetric difference of the two sets. Print the modified first set.

### Assignment 14: Set Membership Testing

Create a set and test if certain elements are present in the set. Print the results.

### Assignment 15: Set of Tuples

Create a set containing tuples, where each tuple contains two elements. Print the set.
'''

# Assignment 11
s = set(range(1, 6))
for elem in s:
    print(elem)

# Assignment 12
rs = {1,2,3,4,5}

while rs:
    rs.pop()
    print(rs)

# Assignment 13
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.symmetric_difference_update(set2)
print(set1)

# Assignment 14
s = set(range(1, 6))
print(3 in s)
print(6 in s)

# Assignment 15
s = { (1, 2), (3, 4), (5, 6) }
print(s)
    
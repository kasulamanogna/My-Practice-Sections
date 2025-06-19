'''# Module 5: Modules and Packages Assignments
## Lesson 5.1: Importing Modules
### Assignment 1: Importing and Using Modules

Import the `math` module and use it to calculate the square root of 25 and the sine of 90 degrees.

### Assignment 2: Aliasing Modules

Import the `datetime` module with an alias and use it to print the current date and time.

### Assignment 3: Importing Specific Functions

Import the `randint` function from the `random` module and use it to generate a random integer between 1 and 100.

### Assignment 4: Importing Multiple Functions

Import the `sqrt` and `pow` functions from the `math` module and use them to calculate the square root of 16 and 2 raised to the power of 3.

### Assignment 5: Handling Import Errors

Write code that attempts to import a non-existent module and gracefully handles the import error by printing an error message.

## Lesson 5.2: Standard Library Overview
### Assignment 6: Working with the `os` Module

Use the `os` module to create a new directory, list the contents of the current directory, and remove the newly created directory.

### Assignment 7: Working with the `sys` Module

Use the `sys` module to print the Python version currently in use and the command-line arguments passed to the script.

### Assignment 8: Working with the `math` Module

Use the `math` module to calculate the greatest common divisor (GCD) of two numbers and the factorial of a number.

### Assignment 9: Working with the `datetime` Module

Use the `datetime` module to print the current date, calculate the date 100 days from today, and determine the day of the week for a given date.

### Assignment 10: Working with the `random` Module

Use the `random` module to generate a list of 5 random numbers between 1 and 50 and shuffle the elements of a list.

## Lesson 5.3: Creating and Using Packages
### Assignment 11: Creating a Simple Package

Create a package named `mypackage` with two modules: `module1` and `module2`. `module1` should contain a function that adds two numbers, and `module2` should contain a function that multiplies two numbers. Write code to use these functions.

### Assignment 12: Using `__init__.py`

Modify the `mypackage` package to include an `__init__.py` file that imports the functions from `module1` and `module2`. Write code to use these functions.

### Assignment 13: Importing from a Package

Write code to import and use the functions from `mypackage` without explicitly importing `module1` and `module2`.

### Assignment 14: Relative Imports

Create a subpackage named `subpackage` within `mypackage` and move `module2` into `subpackage`. Modify the import statements in `__init__.py` to use relative imports. Write code to use the functions from both modules.

### Assignment 15: Handling Package Import Errors

Write code that attempts to import a non-existent function from `mypackage` and gracefully handles the import error by printing an error message.
'''

# Assignment 1

import math

from mypackages.subpackages import module2
print(math.sqrt(25))
print(math.sin(90))

print(math.radians(90))

# Assignment 2
import datetime as dt
print(dt.datetime.now())

# Assignment 3

from random import randint
print(randint(1, 100))

# Assignment 4

from math import sqrt,pow

print(sqrt(16))
print(pow(2, 3))

# Assignment 6

'''import os

os.mkdir('mew_directory')

print(os.listdir('.'))

os.rmdir('new_directory')
print(os.listdir('.'))'''

# Assignment 7

import sys
print (f"python version: {sys.version}")
print(f"Command-line arg: {sys.argv}")

# ASSIGNMENT 8
import math
print(math.gcd(4, 10)) # 2
print(math.factorial(5)) # 120

# Assignment 9
import datetime

today = datetime.date.today()
print(f"Today's date: {today}")

future_date = today + datetime.timedelta(days=100)
print(f"Date 100 days from today: {future_date}")

given_date = datetime.date(2021, 1, 1)
print(given_date)

# Assignment 10

import random

number_random = [random.randint(1, 50) for _ in range(5)]
print(number_random)
#Shuffle a list
lst = [1,2,3,4,5]
random.shuffle(lst)
print(lst)

# Assignment 6

'''import os

# Create a new directory
os.mkdir('old_dir')

# List contents of the current directory
print(os.listdir('.'))

# Remove the newly created directory
os.rmdir('old_dir')
print(os.listdir('.'))'''


# Assignment 11

from mypackages import module1
print(module1.add(2, 3))
print(module2.multiply(5, 2)) 

# Assigment 12

from mypackages import add, multiply

print(add(2, 3)) # 5
print(multiply(2, 3)) # 6

# Assignment 13
from mypackages import add, multiply

print(add(2, 3))  # 5
print(multiply(2, 3))  # 6

# Assignment 14

from mypackages import add, multiply

print(add(2, 3))  # 5
print(multiply(2, 3))  # 6

# Assignment 15

try:
    from mypackages import non_existent_function
except ImportError as e:
    print(f"Error importing function: {e}")



















#!/usr/bin/python3

'''
Write a function that prints a string in uppercase followed by a new line.

Prototype: def uppercase(str):
    Using only no more than 2 print functions with string format
    Use only one loop in the code
    Not allowed to import any module
    Not allowed to use str.upper() and str.isupper()
    Tips: ord()
'''
# Author: Usman Saheed .K

# Define function
def uppercase(str):

    # Different between Uppercase and Lowercase
    dif = ord("a") - ord("A")

    # Loop through characters of str
    for char in str:
        # check each characters if it is Lowercase, Hence convert to uppercase using the 'dif' if condition True
        if char >= 'a' and char <= 'z':
            char = chr(ord(char) - dif)

        # Print by character after each succesfull checkings
        print('{}'.format(char), end='')
    # Print newline
    print()

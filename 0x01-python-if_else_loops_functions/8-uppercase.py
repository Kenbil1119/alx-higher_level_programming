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


def uppercase(str):

    # Empty string to reserve space for uppercase of str
    upper_str = ""

    # Different between Uppercase and Lowercase
    dif = ord("a") - ord("A")

    # Loop through characters of str
    for char in str:
        # check each characters if it is Lowercase, Hence convert to uppercase using the 'dif' if condition True
        if char >= 'a' and char <= 'z':
            upper_str += (chr(ord(char) - dif))
        else:
            upper_str += char

        # Print uppercase version of str
    print("{}".format(upper_str))

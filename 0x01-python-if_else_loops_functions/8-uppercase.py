#!/usr/bin/python3

'''
Write a function that prints a string in uppercase followed by a new line.

Prototype: def uppercase(str):
    You can only use no more than 2 print functions with string format
    You can only use one loop in your code
    You are not allowed to import any module
    You are not allowed to use str.upper() and str.isupper()
    Tips: ord()
    You don’t need to understand __import__
'''
# Author: Usman Saheed .K


def uppercase(str):

    dif = ord('a') - ord('A')
    upper_str = ""
    for char in str:
        if 'a' <= char <= 'z':
            upper_str += chr(ord(char) - dif)
        else:
            upper_str += char

    print('{}'.format(upper_str))

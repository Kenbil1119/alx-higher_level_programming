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

def uppercase(str):

    dif = ord("a") - ord("A")

    list_str = []

    for i in range(len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            list_str.append(chr(ord(str[i]) - dif))
        else:
            list_str.append(str[i])

    print('{}'.format(''.join(list_str)))

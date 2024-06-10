#!/usr/bin/python3

'''
Write a function that prints the last digit of a number.

Prototype: def print_last_digit(number):
    Returns the value of the last digit
    You are not allowed to import any module
    You don’t need to understand __import__

No newline
'''
# Author: Usman Saheed .K


def print_last_digit(num):

    num = int(num)

    if num < 0:
        num = num * -1

    ld = num % 10

    print('{}'.format(ld), end='')

    return ld

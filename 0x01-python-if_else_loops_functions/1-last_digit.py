#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldt = abs(number) % 10
if number < 0:
    ldt *= -1
if ldt > 5:
    print(f"Last digit of {number:d} is {ldt:d} and is greater than 5")
elif ldt == 0:
    print(f"Last digit of {number:d} is {ldt:d} and is 0")
else:
    print(f"Last digit of {number:d} is {ldt:d} and is less than 6 and not 0")

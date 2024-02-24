#!/usr/bin/python3

# single Combination of 2 digit numbers.
# for two digit, the number is less than 100.

for f in range(0, 10):  # 'f' read first digit
    for s in range(f + 1, 10):  # 's' read second digit
        if (f == 8 and s == 9):
            print("{:d}{:d}".format(f, s))
        else:
            print("{:d}{:d}".format(f, s), end=", ")

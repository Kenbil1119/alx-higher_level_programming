#!/usr/bin/python3

# 97 been the unicode (ASCII) of 'a'
# 122 been the unicode of the last lowercase letter of the alphabet
# 101 been the unicode of 'e'
# 113 been the unicode of 'q'

for alpha in range(97, 123):
    if (alpha == 101) or (alpha == 113):
        continue
    print("{:c}".format(alpha), end="")

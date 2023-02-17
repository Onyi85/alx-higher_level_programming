#!/usr/bin/python3
""" This module factorizes numbers into a product of two smaller
    numbers.
"""

import sys

# checking if only the file name is passed as argument
if len(sys.argv) == 1:
    exit()


def fact(num):
    """ This function factorize into product of two smaller num"""

    # starting at the minimum number
    divisor = 2

    # checking for lines with number less than or equal 1
    if num < 2:
        return
    # if num is not even, keep make i be a perfect divisor
    while num % divisor:
        divisor = divisor + 1
    # print a neatly formatted output as whole number
    print("{:.0f}={:.0f}*{:.0f}".format(num, num/divisor, divisor))


try:
    # opening the file name provided as the first argument
    with open(sys.argv[1]) as file:
        # reading line by line
        line = file.readline()
        # checking if line is not empty
        while line != "":
            # converting the string to int
            num = int(line.split('\n')[0])
            # factorizing the number
            fact(num)
            # go to the next line when done
            line = file.readline()
except Exception:
    # if there is any unexpected error, pass
    pass

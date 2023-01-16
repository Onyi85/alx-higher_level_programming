#!/usr/bin/python3
"""
    This module adds only integers and returns them
"""


def add_integer(a, b=98):
    """ This function adds two numbers that are only ints """
    # check if a or b is int or float or else raise TypeError
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return (a + b)

#!/usr/bin/python3
""" This module prints size * #, if size abides by all
conditions.
FILENAME: 4-print_square.py
"""


def print_square(size):
    """ This function prints out a square with the
    character #
    """
    # - - - checking if size is not int
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # - - - checking if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # - - - checking if size is a float and less than 0
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # if everything works fine
    for i in range(size):
        print(size * '#')

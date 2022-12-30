#!/usr/bin/python3
"""This module defines a Square"""


class Square():
    """
        Square: defines a square
        Attributes:
                size: To know the length of sides, area and perimeter

        Method:
                __init__: Initializing the Square attribute

                area: Calculates the area of square
     """
    def __init__(self, size=0):
        """Initializing the instance attribute

        Args:
            Size attributes
        """
        self.__size = size
    # Using property decorator
    # a getter function

    @property
    def size(self):

        """
            size: to return the size attribute
        """
        return self.__size
    # setter function

    @size.setter
    def size(self, value):
        """
            size: To set the size attribute

            Arguments:
                value: an integer or string
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of square"""
        return (self.__size ** 2)

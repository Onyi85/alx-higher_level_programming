#!/usr/bin/python3
"""This module defines a square"""


class Square():
    """
        Square: defines a square

        Attributes:
                Size: To know the length of sides, area and perimeter
        Methods:
                __init__: Initialize the square attributes
    """
    def __init__(self, size=0):
        """
            Initializing the instance attribute

            Args:
                size: size attributes
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

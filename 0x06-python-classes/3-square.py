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
        try:
            if self.__size < 0:
                raise ValueError
        except ValueError:
            print("size must be >= 0")
        except TypeError:
            print("size must be an integer")
        except Exception:
            raise TypeError

    def area(self):
        """Calculates the area of square"""
        return (self.__size ** 2)

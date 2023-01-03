#!/usr/bin/python3
"""This module shows us how to define an empty class"""


class Rectangle:
    """
        This class defines a Rectangle, though it's empty at the moment
    Rectangle: Defines a rectangle
    Attributes:
        width: The longest sides of the rectangle
        height: The shortest sides of the rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializing the attributes"""
        self.width = width
        self.height = height

    # the getter function
    @property
    def width(self):
        """Returns the width object"""
        return self.__width

    # the setter function
    @width.setter
    def width(self, value):
        """Sets the width attribute's value"""
        if type(value) is int and value >= 0:
            self.__width = value
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    # the height's getter function
    @property
    def height(self):
        """Returns the height attribute's value"""
        return self.__height

    # height's setter function
    @height.setter
    def height(self, value):
        """Sets the height attribute's value"""
        if type(value) is int and value >= 0:
            self.__height = value
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """This method calculates and returns area of a rectangle"""
        area_of_rect = self.__width * self.__height
        return area_of_rect

    def perimeter(self):
        """This method calculates and returns the perimeter"""
        if self.__width == 0 or self.__height == 0:
            perimeter_of_rect = 0
        else:
            perimeter_of_rect = 2 * self.__width + 2 * self.__height
        return perimeter_of_rect

    # Setting the print behavior
    def __str__(self):
        """This method is to print class objects"""
        items = ""
        if self.__width == 0 or self.__height == 0:
            return items[:-1]
        for i in range(0, self.__height):
            items += self.__width * "#"
            items += "\n"
        return items[:-1]

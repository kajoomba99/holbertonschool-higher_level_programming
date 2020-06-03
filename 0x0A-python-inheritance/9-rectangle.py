#!/usr/bin/python3
"""
module for Rectangle.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Rewrite entry point"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """return the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        string = "[" + str(type(self).__name__) + "] " +\
            str(self.__width) + "/" + str(self.__height)
        return string

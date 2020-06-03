#!/usr/bin/python3

"""
module for Square.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """Initialize"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        string = "[" + str(type(self).__name__) + "] " +\
            str(self.__size) + "/" + str(self.__size)
        return string

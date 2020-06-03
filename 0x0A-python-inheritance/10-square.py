#!/usr/bin/python3

"""
module for Square.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """Initialize"""
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2

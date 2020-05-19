#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
0. My first square:
Write an empty class Square that defines a square:
You are not allowed to import any module
"""


class Square:
    """Square class - receive the size of an square"""
    def __init__(self, size=0):
        """Init methos receive size attr ans pass it to the class"""
        self.__size = size

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print a # square"""
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)

    @property
    def size(self):
        """get size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size of the square"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

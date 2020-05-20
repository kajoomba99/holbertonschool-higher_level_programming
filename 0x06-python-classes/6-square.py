#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
0. My first square:
Write an empty class Square that defines a square:
You are not allowed to import any module
"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """get value fo size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set value to size"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """get value fo position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set value to position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(value[0], int) or value[0] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(value[1], int) or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """print a square of #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)

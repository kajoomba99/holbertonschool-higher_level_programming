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
        """Init methos recive size attr ans pass it to the class"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

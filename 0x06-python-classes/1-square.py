#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
0. My first square:
Write an empty class Square that defines a square:
You are not allowed to import any module
"""


class Square:
    """Square class - receive the size of an square"""
    def __init__(self, size):
        """Init methos recive size attr ans pass it to the class"""
        self.__size = size

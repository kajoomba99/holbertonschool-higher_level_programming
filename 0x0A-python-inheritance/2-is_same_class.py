#!/usr/bin/python3
"""Thi module contain is_same_class function
"""


def is_same_class(obj, a_class):
    """
        Return True if the object is an instance of, or if the object is an
        instance of a class that inherited from, the specified class;
        otherwise False.
    """
    if type(obj) is a_class:
        return True
    return False

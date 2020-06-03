#!/usr/bin/python3
"""this module contain inherits_from function
"""


def inherits_from(obj, a_class):
    """
        returns True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class ; otherwise False.
    """
    list_A = list(type(obj).mro())
    list_A.remove(type(obj))
    return a_class in list_A

#!/usr/bin/python3
"""LookUp Module
"""


def lookup(obj):
    """return the list of available attributes and methods of an object

    Arguments:
        obj {any typpe} -- Any type
    """
    return (dir(obj))

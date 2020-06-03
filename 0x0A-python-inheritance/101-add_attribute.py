#!/usr/bin/python3
"""
Add attr module
"""


def add_attribute(obj, name, value):
    """
    adds a new attribute to an object if it’s possible
    """
    if type(obj).__name__ in (str, int, float, bool):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)

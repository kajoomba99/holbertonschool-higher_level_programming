#!/usr/bin/python
"""This module contain MyList class"""


class MyList(list):
    """Class tha inherit from list"""

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))

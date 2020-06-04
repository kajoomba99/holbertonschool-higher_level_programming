#!/usr/bin/python3
"""Module
"""


def read_file(filename=""):
    """Function"""
    with open(filename, encoding="utf-8") as a_file:
        print(a_file.read())

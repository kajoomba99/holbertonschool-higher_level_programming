#!/bin/usr/python3
"""Module"""


def append_write(filename="", text=""):
    """Function"""
    ln = 0
    with open(filename, mode="a", encoding="utf-8") as a_file:
        ln = a_file.write(text)
    return ln

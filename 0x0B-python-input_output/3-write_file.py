#!/usr/bin/python3
"""Module"""


def write_file(filename="", text=""):
    """Function"""
    nl = 0
    with open(filename, mode="w", encoding="utf-8") as a_file:
        nl = a_file.write(text)
    return nl

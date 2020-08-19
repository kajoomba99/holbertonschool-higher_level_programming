#!/usr/bin/python3
"""Moule that contain function to find the peak in a list"""


def find_peak(list_of_integers):
    """
    This function returns the peak of a list
    """
    if list_of_integers != []:
        list_of_integers.sort()
        return list_of_integers[-1]

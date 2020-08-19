#!/usr/bin/python3
"""Moule that contain function to find the peak in a list"""


def find_peak(list_of_integers):
    """Find the peak in a list"""
    if not type(list_of_integers) is list or list_of_integers == []:
        return None
    
    return list_of_integers.sort()[-1]

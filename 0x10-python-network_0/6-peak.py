#!/usr/bin/python3
"""Moule that contain function to find the peak in a list"""


def find_peak(list_of_integers):
    """Find the peak in a list"""
    if not type(list_of_integers) is list or list_of_integers == []:
        return None

    peak = 0

    for i in range(len(list_of_integers)):
        if i == 0:
            try:
                if list_of_integers[i] > list_of_integers[i + 1]:
                    if list_of_integers[i] > peak:
                        peak = list_of_integers[i]
            except Exception:
                peak = list_of_integers[i]
        elif i == len(list_of_integers) - 1:
            try:
                if list_of_integers[i] > list_of_integers[i - 1]:
                    if list_of_integers[i] > peak:
                        peak = list_of_integers[i]
            except Exception:
                peak = list_of_integers[i]
        else:
            fc = list_of_integers[i] >= list_of_integers[i - 1]
            sc = list_of_integers[i] >= list_of_integers[i + 1]
            if fc and sc:
                if list_of_integers[i] > peak:
                    peak = list_of_integers[i]
            if list_of_integers[i] > peak:
                peak = list_of_integers[i]
    return peak

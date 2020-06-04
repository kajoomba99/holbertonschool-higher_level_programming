#!/usr/bin/python3
"""Module"""


import json


def load_from_json_file(filename):
    """Function"""
    with open(filename) as json_file:
        return json.load(json_file)

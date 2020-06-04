#!/usr/bin/python3
"""Module"""

def read_lines(filename="", nb_lines=0):
    """Function"""
    number_of_lines = 0
    with open(filename, encoding="utf-8") as a_file:
        for _ in a_file:
            number_of_lines += 1

    with open(filename, encoding="utf-8") as a_file:
        if nb_lines > 0 and nb_lines < number_of_lines:
            for _ in range(nb_lines):
                line = a_file.readline()
                if not line:
                    break
                print(line, end="")
        else:
            print(a_file.read())

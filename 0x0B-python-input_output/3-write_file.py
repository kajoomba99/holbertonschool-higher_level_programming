#!/usr/bin/python3


def write_file(filename="", text=""):
    nl = 0
    with open(filename, mode="w", encoding="utf-8") as a_file:
        nl = a_file.write(text)
    return nl

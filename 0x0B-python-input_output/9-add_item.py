#!/usr/bin/python3
"""Module"""


from sys import argv
from os import path

save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file

file_name = "add_item.json"
my_list = []


if path.exists(file_name) and path.getsize(file_name) > 0:
    my_list = load_from_json_file("add_item.json")
    for i in range(1, len(argv)):
        my_list.append(argv[i])


save_to_json_file(my_list, file_name)

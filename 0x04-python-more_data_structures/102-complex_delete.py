#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i in a_dictionary:
        if a_dictionary[i] == value:
            del_val = a_dictionary.pop(i)
            complex_delete(a_dictionary, del_val)
            break
    return a_dictionary

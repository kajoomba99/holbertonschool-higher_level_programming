#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) == 1:
        fv = tuple_a[0] + tuple_b[0]
        sv = tuple_a[1]
    if len(tuple_b) == 2:
        fv = tuple_a[0] + tuple_b[0]
        sv = tuple_a[1] + tuple_b[1]
    if len(tuple_b) == 0:
        fv = tuple_a[0]
        sv = tuple_a[1]
    return (fv, sv)

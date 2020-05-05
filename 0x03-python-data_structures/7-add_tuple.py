#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 1:
        fv = tuple_a[0]
    else:
        fv = 0
    if len(tuple_b) >= 1:
        fv += tuple_b[0]
    else:
        fv += 0
    if len(tuple_a) >= 2:
        sv = tuple_a[1]
    else:
        sv = 0
    if len(tuple_b) >= 2:
        sv += tuple_b[1]
    else:
        sv += 0
    return (fv, sv)

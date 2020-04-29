#!/usr/bin/env python3
def magic_calculation(a, b, c):
    rv = ''
    if (a < b):
        rv = c
    if (c > b):
        rv = a + b
    else:
        rv = a * b - c
    return (rv)

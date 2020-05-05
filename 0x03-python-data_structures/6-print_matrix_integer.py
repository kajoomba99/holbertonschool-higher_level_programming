#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    nl = '\n'.join([' '.join(['{}'.format(i) for i in r]) for r in matrix])
    print(nl)

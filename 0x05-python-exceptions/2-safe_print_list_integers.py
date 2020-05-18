#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    int_elements = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end='')
            int_elements += 1
        except IndexError:
            raise
        except (ValueError, TypeError):
            pass
    print("")
    return int_elements

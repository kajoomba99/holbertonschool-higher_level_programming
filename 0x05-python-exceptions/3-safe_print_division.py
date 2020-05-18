#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        inside_result = a / b
    except (ZeroDivisionError, TypeError):
        inside_result = None
    finally:
        print("Inside result: {}".format(inside_result))
        return inside_result

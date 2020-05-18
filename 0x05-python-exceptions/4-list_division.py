#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            nv = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            nv = 0
        except TypeError:
            print("wrong type")
            nv = 0
        except IndexError:
            print("out of range")
            nv = 0
        finally:
            new_list.append(nv)
    return new_list

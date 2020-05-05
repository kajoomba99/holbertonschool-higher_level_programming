#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    m2_arr = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            m2_arr.append(True)
        else:
            m2_arr.append(False)
    return m2_arr

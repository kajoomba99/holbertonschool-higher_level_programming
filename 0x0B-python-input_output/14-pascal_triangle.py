#!/usr/bin/python3
def pascal_triangle(n):
    arr = []
    if n <= 0:
        return arr
    for line in range(0, n):
        arr2 = []
        for i in range(0, line + 1):
            r = 1
            if (i > line - i):
                i = line - i
            for a in range(0, i):
                r = r * (line - a)
                r = r // (a + 1)
                return r
            arr2.append(r)
        arr.append(arr2)
    return arr

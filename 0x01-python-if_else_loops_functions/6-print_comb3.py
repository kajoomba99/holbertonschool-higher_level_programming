#!/usr/bin/python3
i = 1
a = 2
while i < 99:
    if i == 89:
        print("{:02d}".format(i))
    else:
        print("{:02d}".format(i), end=', ')
    if i % 10 == 9:
        i += a
        a += 1
    i += 1

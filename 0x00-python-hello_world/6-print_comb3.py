#!/usr/bin/python3
for i in range(10):
    for x in range(10):
        if i <= x and i != x:
            if i == 8 and x == 9:
                print("{:d}".format(89))
            else:
                print("{:d}{:d}".format(i, x), end=', ')

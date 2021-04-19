#!/usr/bin/python3
if __name__ == "__main__":
    from sys import *
    argc = len(argv) - 1
    if argc == 1:
        print("{:d} argument:".format(argc))
    elif argc == 0:
        print("{:d} arguments.".format(argc))
    else:
        print("{:d} arguments:".format(argc))
    if argc:
        for i in range(argc):
            out = [print("{:d}: {}".format(i + 1, argv[i + 1]))]

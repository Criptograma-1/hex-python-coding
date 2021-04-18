#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = int(repr(number)[-1])
if last > 5:
    print("last digit of {:d} is {:d} and is greater than 5".format(number, last))
elif last == 0:
    print("last digit of {:d} is {:d} and is 0".format(number, last))
elif last < 6:
    print("last digit of {:d} is {:d} and is less than 6 and not 0".format(number, last))

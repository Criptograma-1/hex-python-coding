#!/usr/bin/python3
"""
Defines class BaseGeometry
"""


class BaseGeometry:
    """Defines area"""
    def area(self):
        """raises an Exception"""
        raise Exception("area() is not implemented")
    pass

    """Public instance method that validates value"""
    def integer_validator(self, name, value):
        """if `value` isn't a integer than raise a TypeError
           if `value` is less or equal to 0 raise a ValueError
        """
        if Type(value) is not int:
            raise TypeError("<name> must be an integer")
        if (value <= 0):
            raise ValueError("<name> must be greater than 0")

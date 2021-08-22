#!/usr/bin/python3
"""
Defines class BaseGeometry
"""


class BaseGeometry:
    """Defines area"""
    def area(self):
        """raises an Exception"""
        raise Exception("area() is not implemented")

    """Public instance method that validates value"""
    def integer_validator(self, name, value):
        """if `value` isn't a integer than raise a TypeError
           if `value` is less or equal to 0 raise a ValueError
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))

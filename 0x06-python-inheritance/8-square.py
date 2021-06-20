#!/usr/bin/python3
"""Import Rectangle"""

Rectangle = __import__('7-ractangle').Rectangle

"""Defines class Square that inherits from Rectangle"""


class Square:
    """Defines size"""
    def __init__(self, size):
        """`size` must be private
           `size` must be a positive integer
           `size` must be validated by integer_validator
        """
        self.integer_validator("size", size)
        self.__size = size

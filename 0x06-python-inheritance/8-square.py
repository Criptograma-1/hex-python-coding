#!/usr/bin/python3
"""Import Rectangle"""

Rectangle = __import__('7-ractangle').Rectangle

"""Defines class Square that inherits from Rectangle"""


class Square:
    """Define the variable or attribute"""
    def __init__(self, size):
        """Validates the values with integer_validator"""
        self.integer_validator("size", size)
        self.__size = size

#!/usr/bin/python3
"""Import BaseGeometry"""

BaseGeometry = __import__('5-base_geometry').BaseGeometry

"""Defines class Rectangle that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """Define the variable or attribute"""
    def __init__(self, width, height):
        """Validates the values with integer_validator"""
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height

#!/usr/bin/python3
"""import class Rectangle"""

from models.rectangle import Rectangle

"""Defines class Square that inherits from Rectangle"""


class Square(Rectangle):
    """Definition of own methods and attributes"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square object"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return("[Square] ({}) {}/{} - {}.".format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        super().width(self, value)

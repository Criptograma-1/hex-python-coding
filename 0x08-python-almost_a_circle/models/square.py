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
        return(
            "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size
            )
        )

    def update(self, *args, **kwargs):
        """Update this object's attributes"""
        if len(args) > 0:
            attrs = ('id', 'size', 'x', 'y')
            for name, value in zip(attrs, args):
                setattr(self, name, value)
        else:
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

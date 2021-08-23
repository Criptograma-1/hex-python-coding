#!/usr/bin/python3
"""Import class Base"""

from models.base import Base

"""Defines class Rectangle that inherits from Base"""


class Rectangle(Base):
    """Initialize attributes"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Property to retrive value of `width`"""
        return self.__width

    @width.setter
    def width(self, value):
        self.width = value

    @property
    def height(self):
        """Property to retrive value of `width`"""
        return self.__height

    @height.setter
    def height(self, value):
        self.height = value

    @property
    def x(self):
        """Property to retrive value of `width`"""
        return self.__x

    @x.setter
    def x(self, value):
        self.x = value

    @property
    def y(self):
        """Property to retrive value of `width`"""
        return self.__y

    @y.setter
    def y(self, value):
        self.y = value

#!/usr/bin/python3
"""Import class Base"""

from models.base import Base

"""Defines class Rectangle that inherits from Base"""


class Rectangle(Base):
    """Definition of own methods and attributes"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor with private attributes and its validations"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Return area of the rectangle"""
        return self.__width * self.__height

    def update(self, *args, **kwargs):
        """method that assigns an argument to each attibute"""
        if args:
            if len(args) == 5:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            if len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
            if len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
            if len(args) == 2:
                self.id = args[0]
                self.width = args[1]
            if len(args) == 1:
                self.id = args[0]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ Getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x """
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ Getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y """
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def display(self):
        """Print in stdout the rectangle"""
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            for i in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns string representation of rectangle"""
        i, w, h = self.id, self.width, self.height
        x, y = self.x, self.y
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(i, x, y, w, h))

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
            'id': self.id, 'width': self.width, 'height': self.height,
            'x': self.x, 'y': self.y
        }

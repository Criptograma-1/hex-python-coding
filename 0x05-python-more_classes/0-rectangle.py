#!/usr/bin/python3
"""defines class Rectangle"""


class Rectangle:
    """Define the variable or attribute in the principal method"""
    def __init__(self, width=0, height=0):
        """initializes attributes
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        Note:
            ``Args`` section don't include `self` parameter
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if (width < 0):
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if (height < 0):
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """property to retrive value of `width`"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter method
        Args:
            value (int): value to be set
        Raises:
            TypeError: if `value` isn't an integer
            ValueError: if `value` is less than 0
        """
        if (type(value) is not int and type(value) is not float):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value
        return value

    @property
    def height(self):
        """property to retrive value of `height`"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter method
        Args:
            value (int): value to be set
        Raises:
            TypeError: if `value` isn't an integer
            ValueError: if `value` is less than 0
        """

        if (type(value) is not int and type(value) is not float):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
        return value

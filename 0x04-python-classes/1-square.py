#!/usr/bin/python3
"""Creating a class Square"""


class Square:
    """Derives a square"""
    def __init__(self, size=0):
        """initializes attributes
        Args:
            size (int): size of the square
        Note:
            ``Args`` section don't include `self` parameter
        Raises:
            TypeError: if `size` isn't an integer
            ValueError: if `size` is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

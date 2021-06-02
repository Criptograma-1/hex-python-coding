#!/usr/bin/python3
"""Creating a class Square"""


class Square:
    """Derives a square"""
    def __init__(self, size):
        """initializes attributes
        Args:
            size (int): value to initialize `size`
        Note:
            ``Args`` section don't include `self` parameter.
        """
        self.__size = size

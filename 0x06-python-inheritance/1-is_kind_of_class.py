#!/usr/bin/python3
"""
Prototype is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """Defines function"""
    if isinstance(obj, a_class):
        """checks if obj belong to a_class"""
        return True
    return False

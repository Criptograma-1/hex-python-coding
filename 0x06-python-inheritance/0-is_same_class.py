#!/usr/bin/python3
"""
Prototype is_same_class
"""


def is_same_class(obj, a_class):
    """checks if obj belongs to a_class class"""
    if type(obj) is a_class:
        """return true if obj is the same class of a_class, false otherwise"""
        return True
    return False

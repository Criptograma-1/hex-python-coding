#!/usr/bin/python3
"""
Prototype inherits_from
"""


def inherits_from(obj, a_class):
    """Defines function"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        """Checks if the obj is an instance of a class that inherited
        from the a_class"""
        return True
    return False

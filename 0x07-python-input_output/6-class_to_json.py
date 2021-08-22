#!/usr/bin/python3
""" Define function class_to_json
"""


def class_to_json(obj):
    """
    Convert class to dict
    Args:
        obj: object from a class
    Return:
        Object turn to dictionary
    """
    return obj = obj.__dict__

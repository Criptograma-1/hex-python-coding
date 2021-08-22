#!/usr/bin/python3
"""Defines the function"""


def class_to_json(obj):
    """
    Convert class to dict
    Args:
        obj: object from a class
    Return:
        Object turn to dictionary
    """
    return obj = obj.__dict__

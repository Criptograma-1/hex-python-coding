#!/usr/bin/python3
"""Defines the function"""


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    for JSON serialization of an object
    Args:
        obj: a class
    Returns:
        converted class to dictionary
    """
    data = {}
    for attr in obj.__dict__:
        data[attr] = obj.__dict__[attr]
    return data

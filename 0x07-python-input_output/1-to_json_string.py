#!/usr/bin/python3
"""Defines function to_json_string"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).
    Args:
        my_obj (string): string that will be converted to JSON
    Return:
        JSON representation of a string
    """
    return json.dumps(my_obj)

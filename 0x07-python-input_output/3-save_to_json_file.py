#!/usr/bin/python3
"""Defines function save_to_json_file"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.
    Args:
        my_obj: string  that will be converted to JSON
        filename: name of the file where the object will be saved
    Return:
        JSON representation of a string
    """
    with open(filename, 'w') as f:
        return json.dump(my_obj, f)

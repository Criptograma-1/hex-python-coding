#!/usr/bin/python3
"""Define function load_from_json_file"""

import json


def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file".
    Args:
        filename: name of the file to be read.
    Return:
        "JSON file"
    """
    with open(filename, 'r') as f:
        return json.load(f)

#!/usr/bin/python3
"""Create class Base"""

import json


class Base:
    """A base class for handle id"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Intialize a attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

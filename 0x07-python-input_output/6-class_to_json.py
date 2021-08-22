#!/usr/bin/python3

"""Import json"""
import json


def class_to_json(obj):
    """Convert class to dict"""
    obj = obj.__dict__
    return json.dumps(obj)

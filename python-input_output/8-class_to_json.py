#!/usr/bin/python3
"""
module that returns the dictionary description with simple data structure
for JSON serialization of an object
"""


def class_to_json(obj):
    """ Returns the dictionary description with simple data structure. """
    return vars(obj)

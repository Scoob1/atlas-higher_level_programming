#!/usr/bin/python3
"""
Module provides a function to creae an object from JSON file.
"""
import json

def load_from_json_file(filename):
    """
    Creates an Object from a JSON file.

    Args:
    filename (str): the name of the JSON file.

    Returns:
    The python object represented by the JSON data in thte file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

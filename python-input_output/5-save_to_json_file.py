#!/usr/bin/python3
"""
This module provides a function to write an Object to a text file
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON."""
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)

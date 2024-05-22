#!/usr/bin/python3
"""
module that provides a function to return an object represented by JSON string
"""
import json


def from_json_string(my_str):
    """
    Returns an object repesented by JSON string

    Args:
    my_str (str): The JSON string.

    Returns:
    The Python structure represented by thte JSON string.
    """

    return json.loads(my_str)

#!/usr/bin/python3
"""
Base module
"""


class Base:
    """Base class for managing `id` attribute in all future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base instance with an id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

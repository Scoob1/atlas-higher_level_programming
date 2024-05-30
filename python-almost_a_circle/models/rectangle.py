#!/usr/bin/python3
"""Module class Rectangle inherits from class Base"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instances"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

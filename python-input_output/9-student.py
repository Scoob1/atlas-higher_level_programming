#!/usr/bin/python3
"""
module that writes a class Student that defines a student
"""


class Student:
    """ Class describes a student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Dictionary representation of a Student instance """
        return vars(self)

#!/usr/bin/python3
"""
This module defines a Student class and its methods to retrieve
a dictionary representation of the instance.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initialize a new student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.
        If attrs is a list of strings, only the attributes
        with those names will be included.
        Otherwise, all attributes will be included.
        """
        if attrs is None:
            return self.__dict__
        return {key: value
                for key, value in self.__dict__.items()
                if key in attrs}

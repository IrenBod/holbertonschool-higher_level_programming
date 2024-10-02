#!/usr/bin/python3
"""Module defining the Student class."""


class Student:
    """
    Represents a student with attributes for first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list): A list of attribute names
            to retrieve. If None, retrieves all attributes.

        Returns:
            dict: A dictionary representing the
            Student instance with the requested attributes.
        """
        if attrs is None:
            return self.__dict__
        return {key: value for key, value
                in self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        with those from the json dictionary.

        Args:
            json (dict): A dictionary containing key-value pairs
            representing attribute names and their new values.
        """
        for key, value in json.items():
            setattr(self, key, value)

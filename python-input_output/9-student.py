#!/usr/bin/python3
"""
Module that defines a Student class and a method to
retrieve its dictionary representation.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initialize the Student instance.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__


student = Student("John", "Doe", 20)
print(student.to_json())

#!/usr/bin/python3
"""
This module provides a class for creating and serializing custom objects
using the pickle module.
"""
import pickle


class CustomObject:
    """
    A class representing a custom object.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Whether the person is a student.
    """
    def __init__(self, name, age, is_student):
        """
        Initializes a new CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the object's attributes in a readable format.
        """
        print("Name: {}\nAge: {}\nIs Student: {}"
              .format(self.name, self.age, self.is_student))

    def serialize(self, filename):
        """
        Serializes the current instance to a file using pickle.

        Args:
            filename (str): The name of the file to save the object to.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            print(f"Failed to serialize data to {filename}: {e}")
        except pickle.PickleError:
            print("Error occured while Pickling.")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from a file using pickle.

        Args:
            filename (str): The name of the file to load the object from.

        Returns:
            CustomObject: The deserialized object instance.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception as e:
            print("Error occured:", e)
            return None
        except FileNotFoundError:
            print("File not found.")
            return None
        except pickle.UnpicklingError:
            print("Error occured while unPickling.")
            return None

#!/usr/bin/python3
"""This module defines the function 'is_same_class'."""


def is_same_class(obj, a_class):
    '''checks if the object is an instance of the specified
    class, If yes, returns TRUE if no, returns FALSE.
    '''
    return type(obj) is a_class

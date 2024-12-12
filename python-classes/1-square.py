#!/usr/bin/python3
""" Class square with private instance attribute """


class Square():
    """ Class that define a square """
    def __init__(self, size):
        """The size is store as a private attribute"""
        self.__size = size

#!/usr/bin/env python3
"""
This module defines an abstract class Animal and its subclasses Dog and Cat.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class Animal which defines an abstract method sound.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses to return the sound
        made by the animal.
        """
        pass


class Dog(Animal):
    """
    Subclass of Animal that implements the sound method for Dog.
    """

    def sound(self):
        """
        Returns the sound a dog makes.
        """
        return "Bark"


class Cat(Animal):
    """
    Subclass of Animal that implements the sound method for Cat.
    """

    def sound(self):
        """
        Returns the sound a cat makes.
        """
        return "Meow"

#!/usr/bin/env python3
"""
This module defines classes for demonstrating multiple inheritance with Fish, Bird, and FlyingFish.
"""

class Fish:
    """Represents a fish with the ability to swim and live in water."""
    
    def swim(self):
        """Prints a message indicating that the fish is swimming."""
        print("The fish is swimming")
    
    def habitat(self):
        """Prints a message indicating the habitat of the fish."""
        print("The fish lives in water")

class Bird:
    """Represents a bird with the ability to fly and live in the sky."""
    
    def fly(self):
        """Prints a message indicating that the bird is flying."""
        print("The bird is flying")
    
    def habitat(self):
        """Prints a message indicating the habitat of the bird."""
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """Represents a flying fish that can both swim and fly."""
    
    def swim(self):
        """Prints a message indicating that the flying fish is swimming."""
        print("The flying fish is swimming!")
    
    def fly(self):
        """Prints a message indicating that the flying fish is soaring."""
        print("The flying fish is soaring!")
    
    def habitat(self):
        """Prints a message indicating that the flying fish lives in both water and sky."""
        print("The flying fish lives both in water and the sky!")

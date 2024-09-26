#!/usr/bin/env python3
"""
This module demonstrates mixins with a Dragon class
that can swim, fly, and roar.
"""


class SwimMixin:
    """Mixin class that adds swimming ability."""

    def swim(self):
        """Prints a message indicating that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class that adds flying ability."""

    def fly(self):
        """Prints a message indicating that the creature flies."""
        print("The creature flies!")


class RoarMixin:
    """Mixin class that adds roaring ability."""

    def roar(self):
        """Prints a message indicating that the creature roars."""
        print("The dragon roars!")


class Dragon(SwimMixin, FlyMixin, RoarMixin):
    """A class representing a dragon that can swim, fly, and roar."""
    pass

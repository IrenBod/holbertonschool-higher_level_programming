class SwimMixin:
    """Mixin class that provides swimming functionality."""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin class that provides flying functionality."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a Dragon that can swim and fly."""
    def roar(self):
        """Make the dragon roar."""
        print("The dragon roars!")

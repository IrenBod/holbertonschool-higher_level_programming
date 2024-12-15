#!/bin/usr/python3

class Fish:
    """Class representing Fish with swimming behavior."""
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Class representing Bird with flying behavior."""
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing FlyingFish with swimming and flying behaviors."""
    def swim(self):
        """Override the swim method from Fish."""
        print("The flying fish is swimming!")

    def fly(self):
        """Override the fly method from Bird."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Override the habitat method from both Fish and Bird."""
        print("The flying fish lives both in water and the sky!")


# Testing
if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()      # Calls the overridden swim method in FlyingFish
    flying_fish.fly()       # Calls the overridden fly method in FlyingFish
    flying_fish.habitat()   # Calls the overridden habitat method in FlyingFish

    # Investigate Method Resolution Order (MRO)
    print("\nMethod Resolution Order (MRO):")
    print(FlyingFish.mro())

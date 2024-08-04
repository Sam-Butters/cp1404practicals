"""
Unreliable car class.
"""

from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """Version of a car that has a random chance not to perform the drive method."""

    def __init__(self, name, fuel, reliability):
        """Initialise an unreliable car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if reliability is higher than a random integer."""
        if randint(0, 100) > self.reliability:
            distance = 0
            print(f"{self.name} failed to start")
        super().drive(distance)

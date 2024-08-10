"""
Silver service taxi class
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A specialised version of a Taxi which includes fare price based on fanciness."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness=0.0):
        """Initialise a Silver Service Taxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Get the current fare."""
        return self.flagfall + super().get_fare()

    def __str__(self):
        """Return a string representation of a Silver Service Taxi instance."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"


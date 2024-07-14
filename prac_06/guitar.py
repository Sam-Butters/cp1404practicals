"""
CP1404 Prac06 - Guitars!
Sam Butters
Time started: 13:41
Time finished:
"""
CURRENT_YEAR = 2017
VINTAGE_AGE = 50


class Guitar:
    """Represent information about a guitar."""

    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Return the age of a Guitar."""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Determine if a Guitar is considered vintage."""
        if self.get_age() >= VINTAGE_AGE:
            return True
        return False

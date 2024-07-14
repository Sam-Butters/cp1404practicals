"""
CP1404 Prac06 - Guitars!
Sam Butters
Time started: 13:41
Time finished:
"""


class Guitar:
    """Represent information about a guitar."""

    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self, current_year):
        """Return the age of a Guitar."""
        age = current_year - self.year
        return age

    def is_vitage(self, age):
        """Determine if a Guitar is considered vintage."""
        if age >= 50:
            return True
        return False

"""
CP1404 Prac06 - Guitar
Sam Butters
Time started: 13:41
Time finished:
"""
CURRENT_YEAR = 2024
VINTAGE_AGE = 50


class Guitar:
    """Represent information about a guitar."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialize a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Get the age of a guitar based on the CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a Guitar is considered vintage or not based on age."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Determine if a Guitar is considered less than another Guitar based on year."""
        return self.year < other.year

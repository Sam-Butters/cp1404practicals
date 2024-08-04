"""
Band class.
"""


class Band:
    """Band class."""

    def __init__(self, name=""):
        """Initialise the band class."""
        self.name = name
        self.band_members = []

    def add(self, member):
        """Add a member to the band."""
        self.band_members.append(member)

    def __str__(self):
        """Return a string representation of the band name and members."""
        members_string = ', '.join(str(member) for member in self.band_members)
        return f"{self.name} ({members_string})"

    def play(self):
        """For each member of the band, print their name and instrument."""
        for member in self.band_members:
            print(member.play())

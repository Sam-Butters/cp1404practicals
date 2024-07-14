"""
CP1404 Prac06 - Programming Language
Sam Butters
Time started: 12:58
Time finished: 13:31
"""


class ProgrammingLanguage:
    """Classify a programing language."""
    def __init__(self, name="", typing=True, reflection=True, year=0):
        """Initialise a ProgrammingLanguage."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if a language is dynamically typed."""
        if self.typing == "Dynamic":
            return True

    # def has_reflection():
    #     if reflection == "yes":
    #         return True

    def __str__(self):
        """Return a string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} typing, Reflection = {self.reflection}, First appeared in {self.year}"


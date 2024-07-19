"""
CP1404 Prac07 - Project Class
Sam Butters
Start time: 15:09 - pause 1517
Estimated completion time: 15 minutes
Actual completion time:
"""


class Project:
    def __init__(self, name="", start_date="", priority=0, cost_estimate=0.0, completion_percentage=0):
        """Initialise a Project object."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of the Project object."""
        return (
            f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
            f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Compare this project start date to another project start date."""
        return self.start_date < other.start_date

    def update_project(self, new_completion_percentage, new_priority):
        self.completion_percentage = new_completion_percentage
        self.priority = new_priority

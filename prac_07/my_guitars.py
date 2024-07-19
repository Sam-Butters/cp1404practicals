"""
CP1404 Prac07 - My Guitars
Sam Butters
"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read a csv file of guitars, convert them to a guitar object and display as a list."""
    my_guitars = []
    read_file(my_guitars)
    print_guitars(my_guitars)


def read_file(my_guitars):
    """Read a file and append a guitar object to a list."""
    with open(FILENAME, "r") as infile:
        for line in infile:
            guitar = process_data(line)
            if guitar:  # Check if process_data() returned a valid Guitar object
                my_guitars.append(guitar)


def process_data(line):
    """Process a line of guitar data and return a guitar object."""
    parts = line.strip().split(",")
    name = parts[0]
    year = parts[1]
    cost = float(parts[2])
    guitar = Guitar(name, year, cost)
    return guitar


def print_guitars(my_guitars):
    """Print a list of guitars."""
    my_guitars.sort()  # Sort guitars by year
    for guitar in my_guitars:
        print(guitar)


main()

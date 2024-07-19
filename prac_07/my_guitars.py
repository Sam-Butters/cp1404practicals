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
    get_guitar(my_guitars)
    print_guitars(my_guitars)
    save_guitars_to_file(my_guitars)


def save_guitars_to_file(my_guitars):
    """Save a list of guitars to file."""
    with open(FILENAME, "w") as outfile:
        for guitar in my_guitars:
            guitar_data = ",".join([str(guitar.name), str(guitar.year), str(guitar.cost)])
            print(guitar_data, file=outfile)


def get_guitar(my_guitars):
    """Get the details of new guitars from the user."""
    print("Add guitar details: ")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        my_guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("Name: ")


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
    year = int(parts[1])
    cost = float(parts[2])
    guitar = Guitar(name, year, cost)
    return guitar


def print_guitars(my_guitars):
    """Print a list of guitars."""
    max_name_length = max(len(guitar.name) for guitar in my_guitars)
    max_price_length = max(len(f"{guitar.cost:.2f}") for guitar in my_guitars)
    my_guitars.sort()  # Sort guitars by year
    for guitar in my_guitars:
        print(f"{guitar.name:<{max_name_length}} ({guitar.year}), worth ${guitar.cost:{max_price_length}.2f}")


main()

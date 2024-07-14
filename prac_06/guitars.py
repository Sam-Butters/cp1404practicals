"""
CP1404 Prac06 - Guitars
Sam Butters
Time started: 15:40
Time finished: 16.21
"""
from prac_06.guitar import Guitar

guitars = []

name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{guitar} added.")
    name = input("Name: ")

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

max_name_length = max([len(guitar.name) for guitar in guitars])
max_cost_length = max(len(f"${guitar.cost:.2f}") for guitar in guitars)

print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = ""
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    print(
        f"Guitar {i}: {guitar.name:>{max_name_length}} ({guitar.year}), worth ${guitar.cost:>{max_cost_length}.2f} {vintage_string}")

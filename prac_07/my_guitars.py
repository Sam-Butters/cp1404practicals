"""
CP1404 Prac07 - My Guitars
Sam Butters
"""

from guitar import Guitar

my_guitars = []


with open("guitars.csv", "r") as infile:
    for line in infile:
        parts = line.strip().split(",")
        name = parts[0]
        year = parts[1]
        cost = float(parts[2])
        guitar = Guitar(name, year, cost)
        my_guitars.append(guitar)
        # print(my_guitars)

for guitar in my_guitars:
    # print(type(Guitar))
    # print(type(my_guitars))
    print(guitar)

main()

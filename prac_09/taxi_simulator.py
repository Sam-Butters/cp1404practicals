"""
Taxi Simulator
"""

from prac_09 import car
from prac_09 import taxi
from prac_09 import silver_service_taxi


MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            # TODO: add choice function
            pass
        elif choice == "d":
            # TODO: add drive function
            pass
        else:
            print("Invalid option")
        choice = input(">>> ").lower()



main()
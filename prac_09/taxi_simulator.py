"""
Taxi Simulator
"""

from prac_09.car import Car
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            choose_taxi(taxis)
            pass
        elif choice == "d":
            # TODO: add drive function
            pass
        else:
            print("Invalid option")
        choice = input(">>> ").lower()


def choose_taxi(taxis):
    """Choose a taxi from a list."""
    display_taxis(taxis)
    taxi_choice = int(input("Choose taxi: "))
    while taxi_choice < 0 or taxi_choice > len(taxis):
        print("Invalid choice")
        taxi_choice = int(input("Choose taxi: "))
    return taxi_choice


def display_taxis(taxis):
    """Display a numbered list of taxis."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()

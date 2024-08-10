"""
Taxi Simulator
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0.0
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = taxis[choose_taxi(taxis)]
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                total_bill += drive_taxi(current_taxi)
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()


def choose_taxi(taxis):
    """Choose a taxi from a list."""
    display_taxis(taxis)
    taxi_choice = get_valid_input("Choose taxi: ", 0, len(taxis) - 1)
    return taxi_choice


def get_valid_input(prompt, min_value, max_value):
    """Get a valid integer input within a specified range."""
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input(prompt))
            if number < min_value or number > max_value:
                print(f"Invalid choice")
            else:
                is_valid_input = True
                return number
        except ValueError:
            print("Invalid input, please enter a number")


def display_taxis(taxis):
    """Display a numbered list of taxis."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def drive_taxi(current_taxi):
    """Drive a taxi."""
    print("Drive how far?")
    distance = float(input(">>> "))
    current_taxi.drive(distance)
    trip_cost = current_taxi.get_fare()
    print(f"Your {current_taxi.name} trip cost: ${trip_cost:.2f}")
    return trip_cost


main()

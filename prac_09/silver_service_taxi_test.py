"""
Silver Service Taxi Test
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Run tests for the SilverServiceTaxi class"""
    super_fancy_taxi = SilverServiceTaxi("Super Fancy Taxi", 80, 10)
    print(super_fancy_taxi)
    super_fancy_taxi.drive(10)
    print(f"Fare: ${super_fancy_taxi.get_fare():.2f}, should be $127.50")
    print(super_fancy_taxi)

    slightly_fancy_taxi = SilverServiceTaxi("Slightly Fancy Taxi", 80, 2)
    print(slightly_fancy_taxi)
    slightly_fancy_taxi.drive(10)
    print(f"Fare: ${slightly_fancy_taxi.get_fare():.2f}, Should be $29.10")
    print(slightly_fancy_taxi)


main()

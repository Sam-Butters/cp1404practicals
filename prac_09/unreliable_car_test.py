"""
Unreliable car test.
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    """Test some unreliable cars."""
    test_lemon_car()
    test_reliable_car()


def test_lemon_car():
    """Test an unreliable car."""
    lemon_car = UnreliableCar("Lemon", 50, 20)
    print(f"{lemon_car.name}, Fuel: {lemon_car.fuel}, Odometer: {lemon_car.odometer}")
    lemon_car.drive(40)
    print(f"{lemon_car.name}, Fuel: {lemon_car.fuel}, Odometer: {lemon_car.odometer}")


def test_reliable_car():
    """Test a reliable car."""
    # VT Commodore, the king of indestructible cars. Weakpoint: fuel cap
    vt_commodore = UnreliableCar("VT Commodore", 80, 99)
    print(f"{vt_commodore.name}, fuel: {vt_commodore.fuel}, odometer: {vt_commodore.odometer}")
    vt_commodore.drive(100)
    print(f"{vt_commodore.name}, fuel: {vt_commodore.fuel}, odometer: {vt_commodore.odometer}")


main()

"""Practical 2 - Password Stars - Sam Butters"""

PASSWORD_LENGTH = 8


def main():
    """Get and print a password"""
    password = get_password()
    print_password(password)


def print_password(password):
    """Print a line of stars the length of the password."""
    print("*" * len(password))


def get_password():
    """Get a password of a minimum length."""
    password = input("Enter a password: ")
    while len(password) < PASSWORD_LENGTH:
        print(f"Password must be at least {PASSWORD_LENGTH} characters long.")
        password = input("Enter a password: ")
    return password


main()

"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
IS_SPECIAL_CHARACTER_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
MIN_UPPERCASE_CHARACTERS = 1
MIN_LOWERCASE_CHARACTERS = 1
MIN_NUMBERS = 1
MIN_SPECIAL_CHARACTERS = 1


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print(f"\t{MIN_UPPERCASE_CHARACTERS} or more uppercase characters")
    print(f"\t{MIN_LOWERCASE_CHARACTERS} or more lowercase characters")
    print(f"\t{MIN_NUMBERS} or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print(f"\tand {MIN_SPECIAL_CHARACTERS} or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0
    for character in password:
        if character.islower():
            number_of_lower += 1
        if character.isupper():
            number_of_upper += 1
        if character.isdigit():
            number_of_digit += 1
        if character in SPECIAL_CHARACTERS:
            number_of_special += 1
    if number_of_upper < MIN_UPPERCASE_CHARACTERS:
        return False
    if number_of_lower < MIN_LOWERCASE_CHARACTERS:
        return False
    if number_of_digit < MIN_NUMBERS:
        return False
    if IS_SPECIAL_CHARACTER_REQUIRED:
        if number_of_special < MIN_SPECIAL_CHARACTERS:
            return False
    return True


main()

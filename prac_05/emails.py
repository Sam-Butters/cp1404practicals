"""
CP1404 Practical 5 - Emails
Sam Butters

Estimate: 30 minutes
Actual: 40+, took a break and lost count.
"""


def main():
    """Create and print a dictionary of names and emails."""
    email_to_name = {}
    email = input('Enter your email: ')

    while email != "":
        name = determine_name(email)
        email_to_name[email] = name
        email = input('Enter your email: ')
    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def determine_name(email):
    """Determine the name associated with a given email."""
    suggested_name = email.split('@')[0].replace('.', ' ').title()
    name_confirmation = input(f"Is your name {suggested_name}? (Y/n)").upper()
    if name_confirmation == "Y" or name_confirmation == "":
        name = suggested_name
        return name
    else:
        name = input("Enter your name: ").title()
        return name


main()

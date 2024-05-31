"""
CP1404 - Score Menu

Psuedocode:
function main
    display menu
    get choice
    while choice != quit option
        if choice = G
            score = get_valid_score
        else if choice = P
            if score = ''
                dsiplay "No score recorded"
            else
                print score
        else if choice = S
            print_stars
        else
            display error message
        get choice
    display quit message

function get_valid_score
    get score
    while score < 0 or score > 100
        print invalid
        get score
    return score

function print_stars(score)
    stars = score
    print stars

main()
"""


def main():
    """Display a menu and get the user's menu choice."""
    score = ""
    menu = "(G)et score \n(P)rint score \n(S)how stars \n(Q)uit"
    print(menu)
    choice = input(": ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            if score == "":
                print("No score recorded")
            else:
                print(f"Score: {score}")
        elif choice == "S":
            if score == "":
                print("No score recorded")
            else:
                show_stars(score)
        else:
            print("Invalid choice")
        print(menu)
        choice = input(": ").upper()
    print("Thank you for playing")


def get_valid_score():
    """Get a score between 0 and 100."""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def show_stars(score):
    """Print a number of stars based on a user input score."""
    print("*" * score)


main()

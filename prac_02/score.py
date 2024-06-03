"""
CP1404 - Score program with functions
"""

import random


def main():
    """Get a user score and a random score and print their categories."""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    print(f"Your score of {score} is considered {determine_score_category(score)}")
    random_score = random.randint(0, 100)
    print(f"Your random score of {random_score} is considered {determine_score_category(random_score)}")


def determine_score_category(score):
    """Determine the category of a score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()

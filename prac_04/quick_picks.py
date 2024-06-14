"""
Quick pick lottery ticket generator
"""
import random

NUMBERS_PER_GAME = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

# Calculate the width based on the maximum number
number_width = len(str(MAXIMUM_NUMBER))

quantity_of_quick_picks = int(input('How many quick picks? '))
quick_picks_games = []

for i in range(quantity_of_quick_picks):
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_GAME:
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if number not in quick_pick:  # Ensures no repeating numbers
            quick_pick.append(number)
    quick_pick.sort()
    quick_picks_games.append(quick_pick)

for quick_pick in quick_picks_games:
    # Nested {} to match width format to constant value
    print(" ".join(f"{number:{number_width}}" for number in quick_pick))

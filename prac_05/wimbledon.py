"""
CP1404 Practical 5 - Wimbledon

"""
from operator import itemgetter

champion_to_win_number = {}

with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
    for line in in_file:
        data = line.split(",")
        champion = data[2]
        # TODO: rewrite to skip first line containing headings, this will stop the output displaying
        # "Champion at the top"
        # Possibly use readlines instead of for line in infile

        if champion in champion_to_win_number:
            champion_to_win_number[champion] += 1
        else:
            champion_to_win_number[champion] = 1

    print("Wimbledon Champions: ")
    for champion, win_number in champion_to_win_number.items():
        print(f"{champion}: {win_number}")

# TODO: Get the champions list, grab their countries, print countries in alphabetical order with no repeats
# Format should be in capitals and their 3 letter abbreviation

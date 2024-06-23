"""
CP1404 Practical 5 - Wimbledon

"""
from operator import itemgetter

champion_to_win_number = {}
champion_countries = set()

with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
    lines = in_file.readlines()

for line in lines[1:]:
    data = line.split(",")
    champion = data[2]
    country = data[1]
    champion_countries.add(country)
    if champion in champion_to_win_number:
        champion_to_win_number[champion] += 1
    else:
        champion_to_win_number[champion] = 1


print("Wimbledon Champions: ")
for champion, win_number in champion_to_win_number.items():
    print(f"{champion}: {win_number}")

# TODO: Get the champions list, grab their countries, print countries in alphabetical order with no repeats
# Format should be in capitals and their 3 letter abbreviation


print(champion_countries)
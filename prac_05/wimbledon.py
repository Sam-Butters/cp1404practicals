"""
CP1404 Practical 5 - Wimbledon

"""
FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Get data from a file, process and display results."""
    lines = get_records(FILENAME)
    champion_to_win_number, champion_countries = process_data(lines)
    print_results(champion_to_win_number, champion_countries)


def get_records(filename):
    """Read file and return list of lines."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()
    return lines


def process_data(lines):
    """Process data, returning a dictionary and a set."""
    champion_to_win_number = {}
    champion_countries = set()

    for line in lines[1:]:  # Skip the first line (headers)
        data = line.split(",")
        champion = data[CHAMPION_INDEX].strip()
        country = data[COUNTRY_INDEX].strip()
        champion_countries.add(country)
        if champion in champion_to_win_number:
            champion_to_win_number[champion] += 1
        else:
            champion_to_win_number[champion] = 1

    return champion_to_win_number, champion_countries


def print_results(champion_to_win_number, champion_countries):
    """Print the champions and their win numbers, and their respective countries."""
    print("Wimbledon Champions:")
    for champion, win_number in champion_to_win_number.items():
        print(f"{champion}: {win_number}")

    print(f"\nThese {len(champion_countries)} countries have won Wimbledon:")
    countries = ", ".join(sorted(champion_countries))
    print(countries)


main()

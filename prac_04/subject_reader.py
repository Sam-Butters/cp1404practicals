"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read and reformat a file"""
    data = load_data()
    print(data)
    display_subject_details(data)


def load_data():
    """Read data from file and return it as a nested list"""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()
        parts = line.split(",")
        parts[2] = int(parts[2])
        data.append(parts)

    input_file.close()
    return data


def display_subject_details(data):
    """Display formatted subject details"""
    for subject_detail in data:
        subject_name = subject_detail[0]
        lecturer = subject_detail[1]
        number_of_students = subject_detail[2]
        print(f"{subject_name} is taught by {lecturer} and has {number_of_students} students")


main()

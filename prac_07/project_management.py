"""
CP1404 Prac07 - Project Management
Sam Butters
Start time  : 15:17
Break       : 18:14
Start again : 10:20
Finish time : 12:44
Estimated completion time: 90 minutes
Actual completion time: 261 minutes - A humbling but enjoyable exercise
"""
import datetime
from prac_07.project import Project

DEFAULT_FILE = "projects.txt"
MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""


def main():
    """Run the project management program."""
    print("Welcome to Pythonic Project Management")
    projects = []
    load_projects(projects)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILE}")
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            load_projects(projects)
        elif menu_choice == "S":

            save_projects(projects)
        elif menu_choice == "D":
            display_projects(projects)
        elif menu_choice == "F":
            filter_project_dates(projects)
        elif menu_choice == "A":
            add_project(projects)
        elif menu_choice == "U":
            update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        menu_choice = input(">>> ").upper()
    print(f"Would you like to save to {DEFAULT_FILE}?")
    save_choice = input(">>> (Y/n) ").upper()
    if save_choice in ("Y", ""):
        save_projects(projects)
    else:
        print("Your project has not been saved.")
    print("Thank you for using custom-built project management software.")


def filter_project_dates(projects):
    """Filter projects by user chosen date."""
    filter_date = get_valid_date("Show projects that start after date (dd/mm/yyyy): ")
    for project in projects:
        start_date = str(datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date())
        if filter_date < start_date:
            print(project)


def save_projects(projects):
    """Save projects to file"""
    save_file_name = input("Save as:  ")
    if save_file_name == "":
        save_file_name = DEFAULT_FILE
    with open(save_file_name, "w", encoding="utf-8") as outfile:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=outfile)
        for project in projects:
            print(
                f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t"
                f"{project.completion_percentage}", file=outfile)
        print(f"Your projects have been saved as {save_file_name}")


def update_project(projects):
    """Update a selected project's completion percentage and priority."""
    for number, project in enumerate(projects, start=1):
        print(f"{number} {project}")
    project_choice_index = get_valid_number("Project choice: ", 1, len(projects)) - 1
    project_choice = projects[project_choice_index]

    print(f"{project_choice}")

    new_percentage = get_valid_number("New percentage (0-100): ", 0, 100)
    new_priority = get_valid_number("New priority (1-9): ", 1, 9)

    project_choice.update_project(new_percentage, new_priority)


def add_project(projects):
    """Add a project to projects list."""
    print("Let's add a new project")
    name = get_valid_input("Name: ")
    start_date = get_valid_date("Start date (dd/mm/yyyy): ")
    priority = get_valid_number("Priority (1-9): ", 1, 9)
    cost_estimate = get_valid_cost("Cost estimate: ", 0)
    percent_complete = get_valid_number("Percentage complete (0-100): ", 0, 100)
    project = Project(name, start_date, priority, cost_estimate, percent_complete)
    projects.append(project)


def display_projects(projects):
    """Display projects from projects list."""
    print("Incomplete projects:")
    for project in projects:
        if project.completion_percentage != 100:
            print("\t", project)
    print("Completed projects:")
    for project in projects:
        if project.completion_percentage == 100:
            print("\t", project)


def load_projects(projects):
    """Load a project from file."""
    # On the first time running the function (empty projects list), use the default file
    if not projects:
        try:
            file = DEFAULT_FILE
        except FileNotFoundError:
            print(f"{DEFAULT_FILE} not found.")
    else:
        try:
            # Ask the user for a file name, set as default if user hits enter
            file = input("Load file.\nFile name: ")
            print(f"{file} loaded.")
        except FileNotFoundError:
            print(f"File {file} not found., using default file. ({DEFAULT_FILE})")
            file = DEFAULT_FILE

    with open(file, "r", encoding="utf-8") as infile:
        infile.readline()  # Bypass the headings line
        projects.clear()  # Reset the projects list
        for line in infile:
            parts = line.strip().split("\t")
            if len(parts) == 5:  # check the file line is a valid format
                name = parts[0]
                start_date = parts[1]
                priority = int(parts[2])
                estimated_cost = float(parts[3])
                completion_percentage = int(parts[4])
                project = Project(name, start_date, priority, estimated_cost, completion_percentage)
                projects.append(project)
            else:
                print(f"Skipping invalid line: {line}")


def get_valid_date(prompt):
    """Get a valid date in format dd/mm/yyyy, with today's date as default if input is blank."""
    while True:
        date_string = input(prompt).strip()
        if date_string == "":
            # Return today's date if input is blank
            return datetime.date.today().strftime("%d/%m/%Y")
        try:
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            return date.strftime("%d/%m/%Y")
        except ValueError:
            print("Invalid date format. Please enter a date in format dd/mm/yyyy.")


def get_valid_number(prompt, min_value, max_value):
    """Prompt user to enter a valid integer within specified range."""
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            print(f"Input must be between {min_value} and {max_value}. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_valid_input(prompt):
    """Get a non-empty input."""
    value = input(prompt).title()
    while value == "":
        print("Input cannot be blank")
        value = input(prompt).title()
    return value


def get_valid_cost(prompt, min_value):
    """Get non-negative input"""
    while True:
        try:
            value = float(input(prompt))
            if value >= min_value:
                return value
            print(f"Input must be between more than {min_value}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


main()

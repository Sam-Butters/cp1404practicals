"""
CP1404 Prac07 - Project Management
Sam Butters
Start time: 15:17 break: 18:14
            start again at 10:20
Estimated completion time: 90 minutes
Actual completion time:

Pseudocode
---------------------------------------------
DEFAULT_FILE = ?

function load_projects(DEFAULT_FILE)
display menu
load projects function
get menu choice     (- (L)oad projects()
                    - (S)ave projects
                    - (D)isplay projects
                    - (F)ilter projects by date
                    - (A)dd new project
                    - (U)pdate project
                    - (Q)uit)

while menu choice != Q
    if menu choice == L:
        execute load projects function
    elif menu choice == S:
        execute save projects function
    elif menu choice == D:
        execute display projects function
    elif menu choice == F:
        execute filter projects by date function
    elif menu choice == A:
        execute add new project function
    elif menu choice == U:
        execute update project function
    else
        print invalid choice
    display menu
get save choice
if yes
    execute save projects function
display thank you message


function load_projects(file)
    open file for reading
    read first line of file (bypass headings)
    loop through each line of file
        split line into parts (on tab)
        put parts into Project object
        add project to projects list


function save_projects(projects)
    open file for writing
    print headers line
    loop through each project in list
    break the sections, convert to strings, separate with tabs
    print project string to file

function display_projects(projects)
    for each project in projects list
    print project

function filter_projects(projects)
    get date input
    convert date string (from input) to datetime object
    loop through projects list
        convert projects dates to datetime object
        if date input < projects date
            print project

function add_project(projects)
    get name
    get date
    get priority
    get cost estimate
    create new project instance with information
    add project to projects list

function update_project(projects)
    display projects with enumerate
    get project_choice
    display chosen project
    get percentage to add
    get new priority (can be blank)

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
            print("Load projects")  # for testing
            load_projects(projects)
        elif menu_choice == "S":
            print("Save projects")  # for testing
            save_projects(projects)
        elif menu_choice == "D":
            print("Display projects")  # for testing
            display_projects(projects)
        elif menu_choice == "F":
            print("Filter projects by date")  # for testing
            filter_project_dates(projects)
        elif menu_choice == "A":
            print("Add new project")  # for testing
            add_project(projects)
        elif menu_choice == "U":
            print("Update project")  # for testing
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
    # filter_date = datetime.datetime.strptime(filter_date_string, "%d/%m/%Y").date()
    for project in projects:
        start_date = datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date()
        if filter_date < start_date:
            print(project)


def save_projects(projects):
    """Save projects to file"""
    save_file_name = input("Save as:  ")
    if save_file_name == "":
        save_file_name = DEFAULT_FILE
    with open(save_file_name, "w") as outfile:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=outfile)
        for project in projects:
            print(
                f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t"
                f"{project.completion_percentage}", file=outfile)
        print(f"Your projects have been saved as {save_file_name}")
        # return save_file_name


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
    start_date = input("Start date (dd/mm/yyyy): ")  # TODO: error check ddmmyyyy format is correct, can also be blank
    # Use today's date if input is empty
    if start_date == "":
        start_date = str(datetime.date.today().strftime("%d/%m/%Y"))
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
            return f"{DEFAULT_FILE} not found."
    else:
        try:
            file = input("Load file.\nFile name: ")  # Ask the user for a file name, set as default if user hits enter
            print(f"{file} loaded.")
        except FileNotFoundError:
            print(f"File {file} not found., using default file. ({DEFAULT_FILE})")
            file = DEFAULT_FILE

    with open(file, "r") as infile:
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
    """Get a valid date in format dd/mm/yyyy."""
    while True:
        try:
            date_string = input(prompt).strip()
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            return date
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

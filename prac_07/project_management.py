"""
CP1404 Prac07 - Project Management
Sam Butters
Start time: 15:17
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
    # TODO: add save choice
    save_choice = input(">>> (Y/n) ").upper()
    if save_choice == "Y" or save_choice == "":
        save_projects(projects)
    print("Thank you for using custom-built project management software.")


def filter_project_dates(projects):
    """Filter projects by user chosen date."""
    filter_date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.datetime.strptime(filter_date_string, "%d/%m/%Y").date()
    for project in projects:
        start_date = datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date()
        if filter_date < start_date:
            print(project)


def save_projects(projects):
    """Save projects to file"""
    save_file_name = input("Where do you want to save your projects? (filename.txt) ")
    with open(save_file_name, "w") as outfile:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=outfile)
        for project in projects:
            print(
                f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t"
                f"{project.completion_percentage}", file=outfile)


def update_project(projects):
    """Update a selected project's completion percentage and priority."""
    for number, project in enumerate(projects, start=1):
        print(f"{number} {project}")
    project_choice = projects[int(input("Project choice: ")) - 1]
    print(project_choice)
    new_percentage = int(input("New percentage: "))
    new_priority = int(input("New priority: "))
    project_choice.update_project(new_percentage, new_priority)


def add_project(projects):
    """Add a project to projects list."""
    #  TODO: can we add today's date as the default value? eg if start_date = "", date == today's' date
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    # Use today's date if input is empty
    if start_date == "":
        start_date = str(datetime.date.today().strftime("%d/%m/%Y"))
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    percent_complete = int(input("Percentage complete: "))
    project = Project(name, start_date, priority, cost_estimate, percent_complete)
    projects.append(project)


def display_projects(projects):
    """Display projects from projects list."""
    # for project in projects:
    #     print(project)
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
    if not projects:  # Check if projects list is empty to determine if this is the first time running
        file = DEFAULT_FILE
    else:
        file = input("File name: ")  # Ask the user for a file name, set as default if user hits enter
        if file == "":
            file = DEFAULT_FILE
        # TODO: add error checking to ensure file exists
    with open(file, "r") as infile:
        infile.readline()  # Bypass the headings line
        for line in infile:
            parts = line.strip().split("\t")
            name = parts[0]
            start_date = parts[1]
            priority = int(parts[2])
            estimated_cost = float(parts[3])
            completion_percentage = int(parts[4])
            project = Project(name, start_date, priority, estimated_cost, completion_percentage)
            projects.append(project)

            print(project)  # for testing
            # print(projects) # for testing
            # print(parts)  # for testing
            # print(line)  # for testing


main()

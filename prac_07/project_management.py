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
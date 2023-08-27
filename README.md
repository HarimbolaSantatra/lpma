# ABOUT
**lpma**: Local Project MAnager. Manage your local hobbies project.

# Installation
Clone the repo:

    git clone https:githib.com/HarimbolaSantatra/lpma.git
    cd lpma

Install the requirements:

    python -m pip install -r requirements.txt

Copy the executable in your path. It is recommanded to use ~/.local/bin:

    cp lpma ~/.local/bin

User data is a simple json file, stored at _~/.local/state/lpma/data.json_

(Further improvement of the project can be done be all these process into a Makefile.)


# Usage
To list all your project:

    lpma list

To list long format, with more description:

    lpma -l

To show the detail of a particular project, open the list to find the project ID, then use

    lpma desc <project_id>

To add a project:

    lpma add <project_id> [opt]

To remove a project:

    lpma rm <project_id>


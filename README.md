# ABOUT
**lpma**: Local Project MAnager. Manage your local hobbies project.

Are you a relentless programmer with equally relentless procrastination ? Maybe you gave up a project months ago and you want to make sure you will remember the state you left it when you go back. Maybe you have some free time to spend programming, and you have so many project in mind but you can't decide where to start. **lpma** basically lists all your *lost love* and let you compare and decide which one to work one, or which one are you exited about in the moment.

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


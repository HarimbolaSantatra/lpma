# LPMA
**lpma**: Local Project MAnager. Manage your local hobbies project.

Are you a relentless programmer with equally relentless procrastination ? Maybe you gave up a project months ago and you want to make sure you will remember the state you left it when you go back. Maybe you have some free time to spend programming, and you have so many project in mind but you can't decide where to start. **lpma** basically lists all your *lost love* and let you compare and decide which one to work on, or which one are you exited about in the moment.
It also serves as a ToDo list for all your project.


## Installation
Clone the repo:

    git clone https:githib.com/HarimbolaSantatra/lpma.git
    cd lpma

Install the requirements:

    make install
    make

User data is a simple json file, stored at _~/.local/state/lpma/data.json_

## Usage
Show help: `lpma --help`

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

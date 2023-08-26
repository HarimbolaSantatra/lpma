import json
import PrintUtils

FILENAME = "jj.json"

def open_json():
    """
    --------
    Return: dict
        the content of the data file
    """
    file = open(FILENAME, 'r')
    j_dict = json.load(file)
    file.close()
    return j_dict

def print_list(long=False):
    file_dic = open_json()
    PrintUtils.header("List of all project")
    for project in file_dic.values():
        PrintUtils.separator()
        print(("Project").ljust(20), end="")
        print(project["name"])
        print(("Type").ljust(20), end="")
        PrintUtils.print_array_elements(project["type"])
        print(("Technology").ljust(20), end="")
        PrintUtils.print_array_elements(project["technology"])
    PrintUtils.footer()


def print_desc(project_name):
    full_file = open_json()
    try:
        project = full_file[project_name]
        print(f'Project: {project["name"]} ({project_name})')
        print("Path:", project['path'])
        print("Improvement:", project['next-improvement'])
    except KeyError:
        print(f'{project_name} project doesn\'t exist !')
    

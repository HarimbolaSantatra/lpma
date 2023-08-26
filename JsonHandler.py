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
    if not long:
        print_list_short(file_dic)
    else:
        print_list_long(file_dic)
    PrintUtils.footer()

def print_list_short(file_dic):
    for project in file_dic.values():
        PrintUtils.separator()
        PrintUtils.clean_line("Project:", project["name"])
        PrintUtils.clean_line("Type:", project["type"], isArray=True)
        PrintUtils.clean_line("Technology:", project["technology"], isArray=True)

def print_list_long(file_dic):
    for project in file_dic.values():
        PrintUtils.separator()
        PrintUtils.clean_line("Project:", project["name"])
        PrintUtils.clean_line("Type:", project["type"], isArray=True)
        PrintUtils.clean_line("Technology:", project["technology"], isArray=True)

        PrintUtils.clean_line("Path:", project["path"], isPath=True)
        PrintUtils.clean_line("Next Improvement", project["next-improvement"])
        PrintUtils.clean_line("Comment", project["comment"])


def print_desc(project_name):
    full_file = open_json()
    try:
        project = full_file[project_name]
        print(f'Project: {project["name"]} ({project_name})')
        print("Path:", project['path'])
        print("Improvement:", project['next-improvement'])
    except KeyError:
        print(f'{project_name} project doesn\'t exist !')
    

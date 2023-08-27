import json
import PrintUtils

FILENAME = "jj.json"
PROPS = ['name', 'path', 'type', 'nextImprovement', 'technology', 'comment']

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

def print_list_summary():
    file_dic = open_json()
    PrintUtils.header("List of all project")
    for k in file_dic.keys():
        print(f'- {k}')
    PrintUtils.footer()

def print_list(long=False):
    file_dic = open_json()
    PrintUtils.header("List of all project")
    if not long:
        print_list_short(file_dic)
    else:
        print_list_long(file_dic)
    PrintUtils.footer()

def print_list_short(file_dic):
    for key, project in file_dic.items():
        PrintUtils.separator()
        PrintUtils.clean_line("ID:", key)
        PrintUtils.clean_line("Project:", project["name"])
        PrintUtils.clean_line("Type:", project["type"], isArray=True)
        PrintUtils.clean_line("Technology:", project["technology"], isArray=True)

def print_list_long(file_dic):
    for key, project in file_dic.items():
        PrintUtils.separator()
        PrintUtils.clean_line("ID:", key)
        PrintUtils.clean_line("Project:", project["name"])
        PrintUtils.clean_line("Type:", project["type"], isArray=True)
        PrintUtils.clean_line("Technology:", project["technology"], isArray=True)

        PrintUtils.clean_line("Path:", project["path"], isPath=True)
        PrintUtils.clean_line("Next Improvement", project["nextImprovement"])
        PrintUtils.clean_line("Comment", project["comment"])


def print_desc(project_name):
    full_file = open_json()

    # if project exist
    if project_name.lower() in full_file:
        project = full_file[project_name]
        PrintUtils.header("Description")
        PrintUtils.clean_line("Project:", project["name"])
        PrintUtils.clean_line("Path:", project["path"], isPath=True)
        PrintUtils.clean_line("Next Improvement", project["nextImprovement"])
    else:
        PrintUtils.error(f'{project_name} doesn\'t exist !')
    
    PrintUtils.footer()


def add_project(prop, verbose=False):
    """
    Parameter:
    ------------
    prop: dic
        dic containing all the project properties (e.g, name, description, type, path, etc)

    Return
    --------
    null
    """

    # open file in read/write mode
    with open(FILENAME, 'r+') as file:
        data = json.load(file)
        # check if project already exist
        if prop['name'].lower() in data.keys():
            PrintUtils.error("Project already exists !")
            exit(1)
        else:
            data[prop['name'].lower()] = prop
            try:
                file.seek(0)
                json.dump(data, file)
                file.truncate(file.tell())
                PrintUtils.success("Data loaded !")
            except:
                PrintUtils.error("Unknown Error when saving data !")
            if verbose:
                print_desc(prop['name'].lower())


def remove_project(name, verbose):
    with open(FILENAME, 'r+') as file:
        data = json.load(file)
        # check if project exist
        if name not in data.keys():
            PrintUtils.error("Project doesn't exist !")
            exit(1)
        else:
            del data[name]
            file.seek(0)
            json.dump(data, file)
            file.truncate(file.tell())
            PrintUtils.success("Project removed successfully !")
            if verbose:
                print_list()

def edit_project(project_name, prop, verbose=False):
    """
    Parameter:
    ------------
    project_name: str
        name of the project. it's different from prop['name'] which is the new name that the user will give
    prop: dic
        dic containing all the project properties (e.g, name, description, type, path, etc)
    """
    with open(FILENAME, 'r+') as file:
        data = json.load(file)
        # check if project exist
        if project_name.lower() not in data.keys():
            PrintUtils.error("Project doesn't exist !")
            exit(1)
        else:
            # if arg is present, modify it
            for k,v in prop.items():
                data[project_name][k] = v

            # Save data to the file
            try:
                file.seek(0)
                json.dump(data, file)
                file.truncate(file.tell())
                PrintUtils.success("Data loaded !")
            except:
                PrintUtils.error("Unknown Error when saving data !")
            if verbose:
                print_desc(prop['name'].lower())

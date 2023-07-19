import json
import PrintUtils

FILENAME = "jj.json"

def open_json():
    file = open(FILENAME, 'r')
    j_dict = json.load(file)
    file.close()
    return j_dict

def print_list(long=False):
    full_file = open_json()
    
    types = []
    for v in full_file.values():
        types.append(v["type"])
    
    PrintUtils.tabular_line(list(full_file.keys()), types)

def print_desc(project_name):
    full_file = open_json()
    project = full_file[project_name]
    print(f'Project: {project["name"]} ({project_name})')
    print("Path:", project['path'])
    print("Improvement:", project['next-improvement'])
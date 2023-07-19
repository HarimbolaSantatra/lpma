import json

FILENAME = "jj.json"

def open_json():
    file = open(FILENAME, 'r')
    j_dict = json.load(file)
    file.close()
    return j_dict

def get_key(keyName):
    pass

def print_desc(project_name):
    full_file = open_json()
    project = full_file[project_name]
    print(f'Project: {project["name"]} ({project_name})')
    print("Path:", project['path'])
    print("Improvement:", project['next-improvement'])
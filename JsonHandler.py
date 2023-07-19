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
    d = open_json()
    print(d)
    print(f'Project: {d["name"]} ({project_name})')
    print("Path:", d['path'])
    print("Improvement:", d['imp'])
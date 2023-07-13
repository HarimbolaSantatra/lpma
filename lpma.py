import json
import textwrap
import argparse

FILENAME = "jj.json"
VERSION = '1.00'
DESCRIPTION = """ 
Local Project Manager (lpma) handle your local programming project. 
Without argument, list all projects.
"""


def read_file(filename):
    s = ""
    file = open(filename)
    s = file.read()
    file.close()
    return s


def get_value(keyName):
    decoder = json.JSONDecoder()
    j_dict = decoder.decode(s)
    return j_dict[keyName]


def print_header():
    text_wrapper = textwrap.TextWrapper(initial_indent="** ")
    print(text_wrapper.wrap("Welcome to lpma!"))
    exit(0)


def print_version():
    print("Program version:", VERSION)
    exit(0)


def list_less():
    print("List less")
    exit(0)


def list_more():
    print("List more")
    exit(0)


def select(project_name):
    print("Select:", project_name)
    exit(0)


def print_desc(project_name):
    print("Describe:", project_name)
    exit(0)


def add_project(project_name):
    print("Add project:", project_name)
    exit(0)


def rm_project(project_name):
    print("Remove project:", project_name)
    exit(0)


parser = argparse.ArgumentParser(
    prog='lpma.py',
    description=DESCRIPTION,
    epilog='Handle all your local coding project :)'
)

parser.add_argument('project_name', nargs='?', default=' ',
                    help='select a project')
parser.add_argument('-l', '--long', action='store_true',
                    help='list projects in long format')
parser.add_argument('-v', '--version', action='store_true',
                    help='show program version')

subparser = parser.add_subparsers(help='add/describe/remove a project')

add_parser = subparser.add_parser('add')
add_parser.add_argument('project_name', nargs='?', help='name of the project')

desc_parser = subparser.add_parser('desc')
desc_parser.add_argument('project_name', nargs='?', help='name of the project')

rm_parser = subparser.add_parser('rm')
rm_parser.add_argument('project_name', nargs='?', help='name of the project')

# Parent parser
p_args = parser.parse_args()

# Subparsers
add_args = add_parser.parse_args()
desc_args = desc_parser.parse_args()
rm_args = rm_parser.parse_args()

if p_args.version:
    print_version()

if p_args.long:
    list_more()

if add_args.project_name:
    print_desc(add_args.project_name)

if desc_args.project_name:
    add_project(desc_args.project_name)

if rm_args.project_name:
    rm_project(rm_args.rm)

if p_args.project_name == ' ':
    list_less()

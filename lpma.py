import json
import textwrap
import argparse

FILENAME = "jj.json"
VERSION = '1.00'
DESCRIPTION = 'Local Project Manager (lpma) handle your local programming project.'


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
                    help='the name of the project')
parser.add_argument('move', choices=['rock', 'paper', 'scissor'], nargs='?')
parser.add_argument('-l', '--long', action='store_true',
                    help='list project name in long format')
parser.add_argument('add', nargs='?',
                    help='add a new project', metavar='add <project_name>')
parser.add_argument('desc', nargs='?',
                    help='show description of a project', metavar='desc <project_name>')
parser.add_argument('rm', nargs='?',
                    help='remove a project', metavar='rm <project_name>')
parser.add_argument('-v', '--version', action='store_true',
                    help='show program version')

args = parser.parse_args()

if args.version:
    print_version()

if args.desc:
    print_desc('santatra_pro')

if args.add:
    add_project("santatra_pro")

if args.rm:
    rm_project('santatra_pro')

if args.long:
    list_more()

if args.project_name == ' ':
    list_less()

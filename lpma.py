import sys
import argparse
import JsonHandler

VERSION = '1.00'
DESCRIPTION = """ 
Local Project Manager (lpma) handle your local programming project. 
Without argument, list all projects.
"""

def check_arg_len(n, parser):
    if len(sys.argv) <= n:
        parser.print_usage()
        exit(0)


def print_version():
    print("Program version:", VERSION)
    exit(0)


def list_less():
    JsonHandler.print_list()


def list_more():
    print("List more")


def select_project(project_name):
    print("Select:", project_name)


def print_desc(project_name):
    JsonHandler.print_desc(project_name)


def add_project(project_name):
    print("Add project:", project_name)


def rm_project(project_name):
    print("Remove project:", project_name)

def main():
    parser = argparse.ArgumentParser(
        prog='lpma.py',
        description=DESCRIPTION,
        epilog='Handle all your local coding project :)'
    )
        

    parser.add_argument('-v', '--version', action='store_true',
                        help='show program version')

    subparser = parser.add_subparsers(dest='subp_name')

    list_parser = subparser.add_parser('list')
    list_parser.add_argument('-l', '--long', action='store_true',
                        help='list projects in long format')
    list_parser.set_defaults(func=list_less)

    add_parser = subparser.add_parser('add')
    add_parser.add_argument('project_name', help='name of the project')
    add_parser.set_defaults(func=add_project)

    desc_parser = subparser.add_parser('desc')
    desc_parser.add_argument('project_name', help='name of the project')
    desc_parser.set_defaults(func=print_desc)

    rm_parser = subparser.add_parser('rm')
    rm_parser.add_argument('project_name', help='name of the project')
    rm_parser.set_defaults(func=rm_project)

    # Parent parser
    args = parser.parse_args()

    if args.version:
        print_version()

    if args.subp_name == 'list':
        check_arg_len(1, parser)
        if args.long:
            list_more()
        else:
            list_less()
    else:
        check_arg_len(2, parser)
        args.func(args.project_name)

if __name__ == '__main__':
    main()

import sys
import argparse
import JsonHandler
import inputHandler

VERSION = '1.00'
DESCRIPTION = """ 
Local Project Manager (lpma) handle your local programming project. 
Without argument, list all projects.
"""

def check_arg_len_less(n, parser):
    # Check if length of the arg is less than n
    if len(sys.argv) <= n:
        parser.print_usage()
        exit(0)


def print_version():
    print("Program version:", VERSION)
    exit(0)


def list_less():
    JsonHandler.print_list()


def list_more():
    JsonHandler.print_list(long=True)


def select_project(project_name):
    print("Select:", project_name)


def print_desc(project_name):
    JsonHandler.print_desc(project_name)


def add_project(project_prop):
    JsonHandler.add_project(project_prop)


def rm_project(name, verbose):
    JsonHandler.remove_project(project_name, verbose)

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

    # ADD
    add_parser = subparser.add_parser('add')
    add_parser.add_argument('-n', '--name', action='store',
        help='name of the project [REQUIRED]', required=True)
    add_parser.add_argument('-p', '--path', action='store',
        help='local path', required=True)
    add_parser.add_argument('-t', '--type', action='append',
        help='type of the project; e.g, design, database, cli, ...')
    add_parser.add_argument('-T', '--technology', action='append',
        help='technology/framework/library used (e.g, NextJS, Unity, C/C++')
    add_parser.add_argument('-i', '--nextImprovement', action='append',
        help='store further improvement to be done or issue to be fixed')
    add_parser.add_argument('-c', '--comment', action='store',
        help='add comments about the project')
    add_parser.add_argument('-v', '--verbose', action='store_true',
        help='print project description after it is added')
    add_parser.set_defaults(func=add_project)

    desc_parser = subparser.add_parser('desc')
    desc_parser.add_argument('project_name', 
        help='name of the project')
    desc_parser.set_defaults(func=print_desc)

    rm_parser = subparser.add_parser('rm')
    rm_parser.add_argument('project_name', 
        help='name of the project')
    rm_parser.add_argument('-v', '--verbose', action='store_true', 
        help='show result after deletion')
    rm_parser.set_defaults(func=JsonHandler.remove_project)

    # Parent parser
    args = parser.parse_args()

    if args.version:
        print_version()

    if args.subp_name == 'list':
        check_arg_len_less(1, parser)
        if args.long:
            list_more()
        else:
            list_less()
    elif args.subp_name == 'add':
        check_arg_len_less(1, parser)
        prop = {
                "name": args.name,
                "path": args.path,
                "type": inputHandler.handleNone(args.type, value_type='array'),
                "technology": inputHandler.handleNone(args.technology, value_type='array'),
                "nextImprovement": inputHandler.handleNone(args.nextImprovement, value_type='array'),
                "comment": inputHandler.handleNone(args.comment)
                }
        JsonHandler.add_project(prop, verbose=args.verbose)

    elif args.subp_name == 'rm':
        check_arg_len_less(1, parser)
        args.func(args.project_name, args.verbose)

    else:
        check_arg_len_less(2, parser)
        args.func(args.project_name)

if __name__ == '__main__':
    main()

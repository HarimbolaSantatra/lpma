import sys
import argparse
import JsonHandler
import inputHandler

VERSION = '1.00'
DESCRIPTION = """ 
Local Project Manager (lpma) handle your local programming project. 
Without argument, list all projects.
"""


def print_version():
    print("Program version:", VERSION)
    exit(0)


def list_short():
    JsonHandler.print_list_summary()


def list_less():
    JsonHandler.print_list()


def list_more():
    JsonHandler.print_list(long=True)


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
    list_parser.add_argument('-s', '--short', action='store_true',
                        help='list project in very short format')
    list_parser.set_defaults(func=list_less)

    # ADD
    add_parser = subparser.add_parser('add', help="Add a project")
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
    add_parser.set_defaults(func=JsonHandler.add_project)

    desc_parser = subparser.add_parser('desc', help="Print project description")
    desc_parser.add_argument('project_name', 
        help='name of the project')
    desc_parser.set_defaults(func=JsonHandler.print_desc)

    rm_parser = subparser.add_parser('rm', help="Remove a project")
    rm_parser.add_argument('project_name', 
        help='name of the project')
    rm_parser.add_argument('-v', '--verbose', action='store_true', 
        help='show result after deletion')
    rm_parser.set_defaults(func=JsonHandler.remove_project)

    edit_parser = subparser.add_parser('edit', help="Edit a project")
    edit_parser.add_argument('project_name', 
        help='name of the project')
    edit_parser.add_argument('-n', '--name', action='store',
        help='new name')
    edit_parser.add_argument('-p', '--path', action='store',
        help='local path')
    edit_parser.add_argument('-t', '--type', action='append',
        help='type of the project; e.g, design, database, cli, ...')
    edit_parser.add_argument('-T', '--technology', action='append',
        help='technology/framework/library used (e.g, NextJS, Unity, C/C++')
    edit_parser.add_argument('-i', '--nextImprovement', action='append',
        help='store further improvement to be done or issue to be fixed')
    edit_parser.add_argument('-c', '--comment', action='store',
        help='add comments about the project')
    edit_parser.add_argument('-v', '--verbose', action='store_true',
        help='print project description after it is added')
    edit_parser.set_defaults(func=JsonHandler.edit_project)

    # Parent parser
    args = parser.parse_args()

    if args.version:
        print_version()

    if args.subp_name == 'list':
        if args.short:
            list_short()
        elif args.long:
            list_more()
        else:
            list_less()
    elif args.subp_name == 'add':
        prop = {
                "name": args.name,
                "path": args.path,
                "type": inputHandler.handleNone(args.type, value_type='array'),
                "technology": inputHandler.handleNone(args.technology, value_type='array'),
                "nextImprovement": inputHandler.handleNone(args.nextImprovement, value_type='array'),
                "comment": inputHandler.handleNone(args.comment)
                }
        args.func(prop, args.verbose)

    elif args.subp_name == 'rm':
        args.func(args.project_name, args.verbose)

    elif args.subp_name == 'edit':
        prop = {}
        if args.name is not None:
            prop["name"] = args.name
        if args.path is not None:
            prop["path"] = args.path
        if args.type is not None:
            prop["type"] = inputHandler.handleNone(args.type, value_type='array')
        if args.technology is not None:
            prop["technology"] = inputHandler.handleNone(args.technology, value_type='array')
        if args.nextImprovement is not None:
            prop["nextImprovement"] = inputHandler.handleNone(args.nextImprovement, value_type='array')
        if args.comment is not None:
            prop["comment"] = inputHandler.handleNone(args.comment)
        args.func(args.project_name, prop, args.verbose)

    else:
        # If there's no sub command given
        parser.print_usage()

if __name__ == '__main__':
    main()

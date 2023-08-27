import argparse
import inputHandler
import json
import PrintUtils

VERSION = '1.00'
DESCRIPTION = """ 
Local Project Manager (lpma) handle your local programming project. 
Without argument, list all projects.
"""

FILENAME = "data.json"
PROPS = ['name', 'path', 'type',
         'nextImprovement', 'technology', 'comment']


class JsonHandler:
    def __init__(self):
        pass

    def open_json(self):
        """
        --------
        Return: dict
            the content of the data file
        """
        file = open(FILENAME, 'r')
        j_dict = json.load(file)
        file.close()
        return j_dict

    def print_list_summary(self):
        file_dic = self.open_json()
        PrintUtils.header("List of all project")
        for k in file_dic.keys():
            print(f'- {k}')
        PrintUtils.footer()

    def print_list(self, long=False):
        file_dic = self.open_json()
        PrintUtils.header("List of all project")
        if not long:
            self.print_list_short(file_dic)
        else:
            self.print_list_long(file_dic)
        PrintUtils.footer()

    def print_list_short(self, file_dic):
        for key, project in file_dic.items():
            PrintUtils.separator()
            PrintUtils.clean_line("ID:", key)
            PrintUtils.clean_line("Type:", project["type"], isArray=True)
            PrintUtils.clean_line(
                "Technology:", project["technology"], isArray=True)
            PrintUtils.clean_line("Next Improvement",
                                  project["nextImprovement"])

    def print_list_long(self, file_dic):
        for key, project in file_dic.items():
            PrintUtils.separator()
            PrintUtils.clean_line("ID:", key)
            PrintUtils.clean_line("Project:", project["name"])
            PrintUtils.clean_line("Type:", project["type"], isArray=True)
            PrintUtils.clean_line(
                "Technology:", project["technology"], isArray=True)
            PrintUtils.clean_line("Path:", project["path"], isPath=True)
            PrintUtils.clean_line("Next Improvement",
                                  project["nextImprovement"])

    def print_desc(self, id):
        full_file = self.open_json()
        # if project exist
        if id.lower() in full_file:
            project = full_file[id]
            PrintUtils.header("Description")
            PrintUtils.clean_line("Project ID:", id)
            PrintUtils.clean_line("Project Name:", project["name"])
            PrintUtils.clean_line("Path:", project["path"], isPath=True)
            PrintUtils.clean_line(
                "Technology:", project["technology"], isArray=True)
            PrintUtils.clean_line("Type:", project["type"], isArray=True)
            PrintUtils.clean_line("Next Improvement",
                                  project["nextImprovement"])
            PrintUtils.clean_line("Comment", project["comment"])
        else:
            PrintUtils.error(f'The project with id \'{id}\' doesn\'t exist !')
        PrintUtils.footer()

    def add_project(self, prop, verbose=False):
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

    def remove_project(self, id, verbose):
        with open(FILENAME, 'r+') as file:
            data = json.load(file)
            # check if project exist
            if id not in data.keys():
                PrintUtils.error("Project doesn't exist !")
                exit(1)
            else:
                del data[id]
                file.seek(0)
                json.dump(data, file)
                file.truncate(file.tell())
                PrintUtils.success("Project removed successfully !")
                if verbose:
                    self.print_list()

    def edit_project(self, id, prop, verbose=False):
        """
        Parameter:
        ------------
        id: str
            name of the project. it's different from prop['name'] which is the new name that the user will give
        prop: dic
            dic containing all the project properties (e.g, name, description, type, path, etc)
        """
        with open(FILENAME, 'r+') as file:
            data = json.load(file)
            # check if project exist
            if id.lower() not in data.keys():
                PrintUtils.error("Project doesn't exist !")
                exit(1)
            else:
                # if arg is present, modify it
                for k, v in prop.items():
                    data[id][k] = v

                # Save data to the file
                try:
                    file.seek(0)
                    json.dump(data, file)
                    file.truncate(file.tell())
                    PrintUtils.success("Data loaded !")
                except:
                    PrintUtils.error("Unknown Error when saving data !")
                if verbose:
                    self.print_desc(prop['name'].lower())


jsonHandler = JsonHandler()


def print_version():
    print("Program version:", VERSION)
    exit(0)


def list_short():
    jsonHandler.print_list_summary()


def list_less():
    jsonHandler.print_list()


def list_more():
    jsonHandler.print_list(long=True)


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

    # ADD PARSER
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
    add_parser.set_defaults(func=jsonHandler.add_project)

    # DESCRIPTION PARSER
    desc_parser = subparser.add_parser('desc', help="Print project description")
    desc_parser.add_argument('id', 
        help='id of the project')
    desc_parser.set_defaults(func=jsonHandler.print_desc)

    # REMOVE PARSER
    rm_parser = subparser.add_parser('rm', help="Remove a project")
    rm_parser.add_argument('id', 
        help='ID of the project')
    rm_parser.add_argument('-v', '--verbose', action='store_true', 
        help='show result after deletion')
    rm_parser.set_defaults(func=jsonHandler.remove_project)

    # EDIT PARSER
    edit_parser = subparser.add_parser('edit', help="Edit a project")
    edit_parser.add_argument('id', 
        help='ID of the project')
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
    edit_parser.set_defaults(func=jsonHandler.edit_project)

    # PARENT PARSER
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
        args.func(args.id, args.verbose)

    elif args.subp_name == 'desc':
        args.func(args.id)

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

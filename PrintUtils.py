import textwrap, os
from rich import print
from rich.console import Console

# Separators
WHSP = "    "
ASTERIX = "*** "
END_SEP = "="
SEPARATOR = "-"
SEP_LEN = 60


def max_str_len(strs):
    max_len = 0
    for s in strs:
        if len(str(s)) > max_len:
            max_len = len(str(s))
    return max_len


def header(title):
    print()
    welcome = WHSP + title + WHSP
    print(welcome.center(SEP_LEN, END_SEP))


def footer():
    print(END_SEP*SEP_LEN)
    print()


def separator():
    print(SEPARATOR * SEP_LEN)


def print_array_elements(array):
    for el in array:
        if array.index(el) == len(array)-1 :
            # if it is the last element
            print(el, end='\n')
        else:
            print(el, end=', ')

def clean_line(title, txt, isArray=False, isPath=False, separator=20):
    if isPath:
        txt = os.path.abspath(txt)
    if isArray:
        print(title.ljust(separator), end="")
        print_array_elements(txt)
    else:
        print(title.ljust(separator), end="")
        print(txt)

def error(error_msg):
    error_console = Console(stderr=True, style="bold red")
    error_console.print(error_msg)

def success(succ_msg):
    succ_console = Console(style="bold green")
    succ_console.print(succ_msg)

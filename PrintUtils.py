import textwrap
from rich import print

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


def tabular_line(indexes, values):
    if len(indexes) != len(values):
        print("PrintUtils error !")
        exit(-1)
    
    mi = max_str_len(indexes)
    mv = max_str_len(values)

    for i in range(len(indexes)):
        ci = str(indexes[i]).rjust(mi, '.')
        cv = str(values[i])
        print(textwrap.shorten(f'{ci} : {cv}', width=70, initial_indent=WHSP))

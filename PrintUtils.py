import textwrap

WHSP = "    "
ASTERIX = "*** "


def max_str_len(strs):
    max_len = 0
    for s in strs:
        if len(str(s)) > max_len:
            max_len = len(str(s))
    return max_len


def header():
    welcome = WHSP + "Welcome to lpma!" + WHSP
    print(welcome.center(40, '='))


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

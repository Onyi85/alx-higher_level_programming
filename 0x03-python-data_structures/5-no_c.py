#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for i in my_string:
        if i == 'c':
            pass
        elif i == 'C':
            pass
        else:
            str = str + i
    return str

#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    newlist = list(a_dictionary)
    if key in newlist:
        a_dictionary[key] = value
    elif key not in newlist:
        a_dictionary[key] = value
    return a_dictionary

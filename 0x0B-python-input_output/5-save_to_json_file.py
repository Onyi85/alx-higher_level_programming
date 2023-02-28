#!/usr/bin/python3
""" This module writes a json format to a file """


import json
""" importing the json module """


def save_to_json_file(my_obj, filename):
    """ This function writes a json format to a file """
    with open(filename, 'w') as fp:
        fp.write(json.dumps(my_obj))
